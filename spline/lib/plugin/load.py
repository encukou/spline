"""Functionality used by Spline core to load and otherwise manipulate plugins.
Plugins themselves should never need to touch anything in this module!
"""

from pkg_resources import iter_entry_points

from pylons import config

import spline.model

def load_plugins():
    """Loads all available plugins and sticks the configuration they offer into
    `spline.plugins.*` keys in the given config dictionary.
    """

    plugins = {}        # plugin_name => plugin
    controllers = {}    # controller_name => controller
    hooks = {}          # hook_name => { priority => [functions] }
    for ep in iter_entry_points('spline.plugins'):
        plugin_class = ep.load()
        plugin = plugin_class()
        plugins[ep.name] = plugin

        # Get list of controllers
        for name, cls in plugin.controllers().iteritems():
            controllers[name] = cls

        # Get list of model classes and inject them into model module
        for cls in plugin.model():
            setattr(spline.model, cls.__name__, cls)

        # Register some hooks
        for name, priority, function in plugin.hooks():
            if not name in hooks:
                hooks[name] = {}
            if not priority in hooks[name]:
                hooks[name][priority] = []

            hooks[name][priority].append(function)

    config['spline.plugins'] = plugins
    config['spline.plugins.controllers'] = controllers
    config['spline.plugins.hooks'] = hooks

def run_hooks(name, *args, **kwargs):
    """Runs the hooks registered for the given name, in priority order, passing
    along all other arguments.
    """

    all_hooks = config['spline.plugins.hooks']

    if not name in all_hooks:
        # No hooks; bail
        return
    hooks = all_hooks[name]

    for priority in [1, 2, 3, 4, 5]:
        if not priority in hooks:
            # Nothing for this priority; bail
            continue

        for function in hooks[priority]:
            function(*args, **kwargs)

    return

