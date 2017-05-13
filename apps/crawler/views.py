# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django.urls import reverse

from . import forms


class MainView(FormView):
    template_name = 'main.html'
    form_class = forms.SearchForm

    def get_success_url(self):
        return reverse('main_view')


main_view = MainView.as_view()
