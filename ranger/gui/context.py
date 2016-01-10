# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

CONTEXT_KEYS = ['reset', 'error', 'badinfo',
        'in_browser', 'in_statusbar', 'in_titlebar', 'in_console',
        'in_pager', 'in_taskview',
        'directory', 'file', 'hostname',
        'executable', 'media', 'link', 'fifo', 'socket', 'device',
        'video', 'audio', 'image', 'media', 'document', 'container',
        'selected', 'empty', 'main_column', 'message', 'background',
        'good', 'bad',
        'space', 'permissions', 'owner', 'group', 'mtime', 'nlink',
        'scroll', 'all', 'bot', 'top', 'percentage', 'filter',
        'flat', 'marked', 'tagged', 'tag_marker', 'cut', 'copied',
        'help_markup', # COMPAT
        'seperator', 'key', 'special', 'border', # COMPAT
        'title', 'text', 'highlight', 'bars', 'quotes', 'tab', 'loaded',
        'keybuffer',
        'infostring',
        'vcsfile', 'vcsremote', 'vcsinfo', 'vcscommit',
        'vcsconflict', 'vcschanged', 'vcsunknown', 'vcsignored',
        'vcsstaged', 'vcssync', 'vcsbehind', 'vcsahead', 'vcsdiverged']

CONVERSION_MAP = dict(
    is_directory='directory',
    is_image='image',
    is_media='media',
    is_socket='socket',
    is_device='device',
    is_video='video',
    is_audio='image',
    is_document='document',
    is_container='container',
)

class Context(object):
    def __init__(self, keys):
        # set all given keys to True
        d = self.__dict__
        for key in keys:
            if key in CONVERSION_MAP:
                key = CONVERSION_MAP[key]
            d[key] = True

# set all keys to False
for key in CONTEXT_KEYS:
    setattr(Context, key, False)
