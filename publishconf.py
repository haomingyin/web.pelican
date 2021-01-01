#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


AUTHOR = 'Haoming Yin'
SITENAME = "Haoming's Console"
SITEURL = "https://haomingyin.com"
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'

# Theme config
THEME = 'themes/brutalist'
FIRST_NAME = 'Haoming'
SITEDESCRIPTION = 'A place where I note down my ideas.'
FAVICON = 'favicon'
LOGO = 'profile.png'
MENUITEMS = [('Tags', '/tags')]
GITHUB = 'https://github.com/haomingyin'
DISQUS_SITENAME = 'haomingyin'

DEFAULT_PAGINATION = 15

# If your site is available via HTTPS, make sure SITEURL begins with https://


DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "haomingyin"
