# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import render

from . import elasticsearch


class MainView(TemplateView):
    """Main view for search photos by tag.
    """
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        error = ''
        result = ''
        if not q:
            error = "empty input"
        else:
            result = self.search_photos(q)
        context = {'error': error, 'tag': q, 'result': result}
        return render(request, self.template_name, context)

    @staticmethod
    def search_photos(tag):
        """Search photos in collected media by Elasticsearch.
        """
        es = elasticsearch.Elasticsearch()
        result = es.search_media(tag)
        photos = [hit['_source']['image_url'] for hit in result['hits']['hits']]
        return photos

    def get_success_url(self):
        return reverse('main_view')


main_view = MainView.as_view()
