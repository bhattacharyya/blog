#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Shantanu Bhattacharyya'
SITENAME = u'Exploring Data'
SITEURL = 'bhattacharyya.github.io'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('dataisbeautiful', 'https://www.reddit.com/r/dataisbeautiful'),
          ('kaggle competitions', 'https://www.kaggle.com/competitions'),)

# Social widget
SOCIAL = (('LinkedIn page', 'https://www.linkedin.com/in/bhattacharyya'),
          ('twitter: @ssb_scripps', 'https://twitter.com/ssb_scripps'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/tuxlite_zf"

OUTPUT_PATH = 'output/'

DISQUS_SITENAME = "esesbee"

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
