#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lei Li'
SITENAME = 'SciLife'
SITEURL = ''
CC_LICENSE = 'CC-BY-NC-SA'
DEFAULT_CATEGORY = 'BlaBla'
PATH = 'content'
OUTPUT_PATH = 'output/'
TIMEZONE = 'Asia/Shanghai'
LOAD_CONTENT_CACHE = False

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
PLUGINS = ['summary']
PLUGIN_PATHS = ['pelican-plugins/summary']
SUMMARY_END_MARKER = "<!--break-->"
SUMMARY_USE_FIRST_PARAGRAPH = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Sidebar
# HIDE_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# Publish Setting
ARTICLE_URL = 'posts/{category}/{date:%Y}/{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}-{date:%d}-{slug}/index.html'

# The URL to refer to an article draft.
DRAFT_URL = 'drafts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'	
DRAFT_SAVE_AS = 'drafts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'


# Pygments Setting for Markdown
MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)', 'extra']

# Pytgments style set by Bootstrap3
PYGMENTS_STYLE = "monokai"

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['assets', 'extra']

#################
# Theme Related #
#################
# THEME = 'pelican-themes/simple-bootstrap'
THEME = 'pelican-bootstrap3-dev'
BOOTSTRAP_THEME = 'cosmo'
# DISPLAY_ARTICLE_INFO_ON_INDEX = True
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

CUSTOM_CSS = 'static/custom.css'
