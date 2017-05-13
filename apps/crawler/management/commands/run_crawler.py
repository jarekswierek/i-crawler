# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from crawler import crawler


class Command(BaseCommand):
    def handle(self, *args, **options):
        cr = crawler.Crawler()
        cr.run()
