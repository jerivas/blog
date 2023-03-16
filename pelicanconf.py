AUTHOR = 'Ed Rivas'
SITENAME = 'Ed Rivas: Blog'
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

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URLs
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL =  PAGE_URL = '{path_no_ext}'
ARTICLE_SAVE_AS =  PAGE_SAVE_AS = '{path_no_ext}/index.html'
CATEGORY_URL = 'category/{slug}'
TAG_SAVE_AS = AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = ''
USE_FOLDER_AS_CATEGORY = False

THEME = "elegant"

# Social
DEFAULT_CATEGORY = "Miscellaneous"
SOCIAL = (
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    ("Twitter", "https://twitter.com/je92rivas"),
    ("Mastodon", "https://indieweb.social/@jerivas"),
)
DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "404"]
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"

# Legal
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

# SEO
SITE_DESCRIPTION = (
    "Ed Rivas' blog on technology, programming, and varied personal topics."
)

LANDING_PAGE_TITLE = "About Me"
