#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'YesWeAreCoding'
SITENAME = 'Bitten By Python'
SITEURL = 'http://www.bittenbypython.com'
#SITEURL = ''
SITELOGO = 'theme/img/ninja.png'
SITETITLE = 'Bitten By Python'
SITEDESCRIPTION = 'Un (autre) blog sur Python'

THEME = 'Flex'
PATH = 'content'
TIMEZONE = 'Europe/Paris'

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS =['../plugins']
PLUGINS = ['i18n_subsites', 'ipynb.markup', 'extract_toc']
IPYNB_IGNORE_CSS = True
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_FR'
LOCALE = 'fr_FR'
I18N_TEMPLATES_LANG = 'en'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_NAME = 'YesWeAreCoding'
COPYRIGHT_YEAR = 2017

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'

ADD_THIS_ID = 'ra-5a34c2ac2c1ffc84'
DISQUS_SITENAME = 'bittenbybypthon'
GOOGLE_ANALYTICS = 'UA-111329786-1'

# Blogroll
# LINKS = (('<i class="fa fa-envelope-o" aria-hidden="true" fa-3x></i> Email', 'mailto:yeswearecoding@gmail.com'),
#         ('<i class="fa fa-github" aria-hidden="true" fa-3x></i> Github', 'https://github.com/yeswearecoding'),
#         ('<i class="fa fa-codepen" aria-hidden="true"></i> Hackerrank', 'https://www.hackerrank.com/yeswearecoding'),)
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope-o', 'mailto:yeswearecoding@gmail.com'),
            ('github', 'https://github.com/yeswearecoding'),
            ('rss', 'http://www.bittenbypython.com/feeds/all.rss.xml'),)

MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

PYGMENTS_STYLE = 'monokai'

