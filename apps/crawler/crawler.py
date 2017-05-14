# -*- coding: utf-8 -*-
import json

import requests

from django.conf import settings

from . import elasticsearch


class Crawler(object):
    """Class for collecting photos from Instagram.
    """
    recent_media_url = '/'.join([
        settings.INSTAGRAM_API_URL,
        'users/{user_id}/media/recent/?access_token={token}'
    ])
    likes_url = '/'.join([
        settings.INSTAGRAM_API_URL,
        'media/{media_id}/likes?access_token={token}'
    ])
    comments_url = '/'.join([
        settings.INSTAGRAM_API_URL,
        'media/{media_id}/comments?access_token={token}'
    ])

    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__(*args, **kwargs)
        with open(settings.INSTAGRAM_KEYS) as data_file:
            keys = json.loads(str(data_file.read()))
        self.token = keys['token']
        self.user = keys['user_id']
        self.checked_users = set()
        self.users_for_check = set()
        self.elasticsearch = elasticsearch.Elasticsearch()

    def run(self):
        """Start collecting media from Instagram.
        """
        self.users_for_check.add(self.user)
        iterate = True
        while iterate is True:
            user_id = self.users_for_check.pop()
            recent_media = self.get_recent_media(user_id)
            self.checked_users.add(user_id)
            for media in recent_media['data']:
                media_id = media['id']
                media_url = media['images']['standard_resolution']['url']
                media_tags = media['tags']

                # save photo
                self.elasticsearch.create_media(media_id, media_url, media_tags)
                print('Saved photo:{url}'.format(url=media_url))

                comments = self.get_comments_by_media_id(media['id'])
                likes = self.get_likes_by_media_id(media['id'])
                for comment in comments['data']:
                    user = comment['from']['id']
                    if user not in self.checked_users:
                        self.users_for_check.add(user)
                for like in likes['data']:
                    user = like['id']
                    if user not in self.checked_users:
                        self.users_for_check.add(user)
            if len(self.users_for_check) < 1:
                iterate = False

    def get_recent_media(self, user_id='self'):
        """Get user recent media.
        """
        url = self.recent_media_url.format(user_id=user_id, token=self.token)
        resp = requests.get(url)
        content = json.loads(str(resp.content.decode('utf-8')))
        return content

    def get_likes_by_media_id(self, media_id):
        """Get likes from photo.
        """
        url = self.likes_url.format(media_id=media_id, token=self.token)
        resp = requests.get(url)
        content = json.loads(str(resp.content.decode('utf-8')))
        return content

    def get_comments_by_media_id(self, media_id):
        """Get comments from photo.
        """
        url = self.comments_url.format(media_id=media_id, token=self.token)
        resp = requests.get(url)
        content = json.loads(str(resp.content.decode('utf-8')))
        return content
