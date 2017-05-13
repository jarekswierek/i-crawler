# -*- coding: utf-8 -*-
import elasticsearch


class Elasticsearch(object):
    es = elasticsearch.Elasticsearch()

    def create_media(self, image_url, tags):
        self.es.index(index='media', doc_type='photos', body={
            'image_url': image_url,
            'tags': tags
        })

    def search_media(self, tag):
        query = 'tags:"{tag}"'.format(tag=tag)
        result = self.es.search(index='media', q=query)
        return result
