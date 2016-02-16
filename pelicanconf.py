#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'YOUR NAME'
SITENAME = u'YOUR SITE NAME'
# leave SITEURL blank when developing
SITEURL = ''

PATH = 'content'

# avoid processing .html files
READERS = {'html': None}

# mix articles and static files in the same place
# @see https://github.com/getpelican/pelican/issues/1587
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['articles', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/yezi.png': {'path': 'favicon.ico'},}

# modify TIMEZONE to your timezone
TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'

# @see http://docs.getpelican.com/en/latest/settings.html#basic-settings
# @see http://docs.getpelican.com/en/latest/settings.html#path-metadata
PATH_METADATA = 'articles/(?P<date>\d{4}/\d{2}/\d{2})/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'

# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# https://github.com/getpelican/pelican/issues/1513
# {tag}tagName syntax not working now
# Update: 3.6.3 looks working now

THEME = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites',
           'edit_on_github',
           'embed_github_repository_file',
           'embed_picasaweb_image']

# custom setting for HTML meta info
META_KEYWORDS = 'YOUR META KEYWORDS'
META_DESCRIPTION = 'YOUR META DESCRIPTION'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
  'zh': {
    'SITENAME': '您的中文站名',
    'AUTHOR': '您的姓名',
    'LOCALE': 'zh_TW.UTF-8',
    'META_KEYWORDS': 'YOUR zh META KEYWORDS',
    'META_DESCRIPTION': 'YOUR zh META DESCRIPTION',
  },
  'th': {
    'SITENAME': 'ชื่อไซต์ของคุณ',
    'AUTHOR': 'ชื่อของคุณ',
    'LOCALE': 'th_TH.UTF-8',
    'META_KEYWORDS': 'YOUR th META KEYWORDS',
    'META_DESCRIPTION': 'YOUR th META DESCRIPTION',
  },
}
I18N_UNTRANSLATED_ARTICLES = 'remove'

# generate only index.html and pages and articles. (no archives, tags, categories)
#DIRECT_TEMPLATES = ['index']
# use metadata attribute 'order' in page files for ordering
# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
PAGE_ORDER_BY = 'order'

# CONTENT_DIR_URL is the setting for edit_on_github plugin
CONTENT_DIR_URL = u'https://github.com/USERNAME/REPO/tree/master/content'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom Jinja2 filter
def hidden_pages_get_page_with_slug_index(hidden_pages):
    for page in hidden_pages:
        if page.slug == "index":
            return page

JINJA_FILTERS = {
    "hidden_pages_get_page_with_slug_index": hidden_pages_get_page_with_slug_index,
}
