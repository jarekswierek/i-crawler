# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import main_view

urlpatterns = [
    url(r'^$', main_view, name='main_view')
]
