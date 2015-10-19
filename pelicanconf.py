#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ahui'
AUTHOR_EMAIL = u'437177786@qq.com'
SITENAME = u"ahui'Blog"
SITEURL = 'http://xiaahui.github.io'
DEFAULT_DATE_FORMAT=('%Y-%m-%d')

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Coursera','http://www.coursera.org'),
         ('homework','http://cs.nju.edu.cn/zlj/Courses.html'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/xiaahui'),
          ('Twitter','https://twitter.com/437177786'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#Disqus
DISQUS_SITENAME = u"xiaahui"

#Theme
THEME = "pelipress"
