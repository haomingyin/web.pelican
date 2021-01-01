#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Haoming Yin'
SITENAME = "Haoming's Console"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'

# Theme config
THEME = 'themes/brutalist'
SITEDESCRIPTION = 'A place where I note down my ideas.'
FAVICON = 'profile.png'
LOGO = 'profile.png'
FIRSTNAME = 'Haoming'
MENUITEMS = [('tags', '/tags')]
GITHUB = 'https://github.com/haomingyin'
DISQUS_SITENAME = 'haomingyin'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
