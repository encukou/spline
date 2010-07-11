"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
from pylons import url
from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *
from webhelpers.pylonslib import Flash

import re


_flash = Flash()
def flash(message, icon=None, **extras):
    """Custom add-to-flash function that supports remembering an optional icon
    per message.
    """
    # Messages are stored as (message, dict_of_extra_stuff)
    if icon:
        extras['icon'] = icon

    _flash((message, extras))

def static_uri(plugin_name, path, **url_kwargs):
    """Takes the name of a plugin and a path to a static file.

    Returns a full URI to the given file, as owned by the named plugin.
    """

    root_url = url('/', **url_kwargs)
    return "%sstatic/%s/%s" % (root_url, plugin_name, path)

def h1(title, id=None, tag='h1', **attrs):
    """Returns an <h1> tag that links to itself.

    `title` is the text inside the tag.

    `id` is the HTML id to use; if none is provided, `title` will be munged
    into something appropriate.
    """
    if not id:
        # See: http://www.w3.org/TR/html4/types.html#type-id
        id = re.sub('[^-A-Za-z0-9_:.]', '-', title.lower())
        if not re.match('[a-zA-Z]', id[0]):
            id = 'x' + id

    link = HTML.a(title, href='#' + id, class_='subtle')
    return HTML.tag(tag, link, id=id, **attrs)

def h2(title, id=None, **attrs):
    """Similar to `h1`, but for an <h2>!"""
    return h1(title, id=id, tag='h2', **attrs)

# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password
