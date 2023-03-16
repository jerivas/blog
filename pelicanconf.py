AUTHOR = 'Ed Rivas'
SITENAME = 'Ed Rivas Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/El_Salvador'

DEFAULT_LANG = 'en'

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

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL =  PAGE_URL = '{path_no_ext}'
ARTICLE_SAVE_AS =  PAGE_SAVE_AS = '{path_no_ext}/index.html'
USE_FOLDER_AS_CATEGORY = False
