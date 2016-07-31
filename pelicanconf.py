#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lei Li'
SITENAME = 'SciLife'
SITEURL = ''
CC_LICENSE = 'CC-BY-NC-SA'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'
DEFAULT_DATE = (2016, 7, 13, 12, 1, 1)
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'pelican-themes/simple-bootstrap'
THEME = 'pelican-bootstrap3-dev'
BOOTSTRAP_THEME = 'cosmo'

# Sidebar
# HIDE_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True