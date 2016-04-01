#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Paul Logston'
SITENAME = 'douglogston.life'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

ARTICLE_URL = ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = PAGE_SAVE_AS = 'pages/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/basic/'

GITHUB_URL = 'https://github.com/douglogston/douglogston'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

