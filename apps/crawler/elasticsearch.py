# -*- coding: utf-8 -*-
import elasticsearch


class Elasticsearch(object):
    es = elasticsearch.Elasticsearch()

    def create_media(self, media_id, image_url, tags):
        self.es.index(index='media', doc_type='photos', id=media_id, body={
            'image_url': image_url,
            'tags': tags
        })

    def search_media(self, tag):
        query = 'tags:"{tag}"'.format(tag=tag)
        result = self.es.search(index='media', q=query)
        return result

    def delete_media(self, media_id):
        self.es.delete(index='media', doc_type='photos', id=media_id)
