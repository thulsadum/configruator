# NOTE local imports are not supported, problem?

from configparser import ConfigParser
from functools import wraps

# DEFAULT_CONFIG = ConfigParser()
# CONFIG = ConfigParser()
# DEFS = dict()


class ConfigContext:
    def __init__(self):
        self.default_config = ConfigParser()
        self.config = ConfigParser()
        self.defs = dict()


_current_context = ConfigContext()


def get_default_context():
    return _current_context


def write_default_config(fp, *, context = _current_context):
    """Writes the default configuration to the given file pointer.

    :param fp file pointer to write to.
    """
    context.default_config.write(fp)


def Config(section, name, *, default=None, arg_name=None, accessor='get', context=_current_context):

    """Decorator to bind configuration keys to function arguments"""

    key = f"{section}.{name}"

    if not arg_name:
        arg_name = name

    if key in context.defs.keys():
        raise ValueError(f"Option '{name}' in section '{section} already defined in {context.defs[key]}.")

    if not context.default_config.has_section(section):
        context.default_config.add_section(section)

    if not context.config.has_section(section):
        context.config.add_section(section)

    if context.default_config.has_option(section,name):
        raise ValueError("Option already defined!")

    context.default_config.set(section, name, default)

    if not context.config.has_option(section, name):
        context.config.set(section, name, default)

    def the_decorator(fun):
        context.defs[key] = f"{fun.__module__}.{fun.__name__}"
        @wraps(fun)
        def the_fun(*args, **kwargs):
            kwargs[arg_name] = getattr(context.config, accessor)(section, name, fallback=default)
            return fun(*args, **kwargs)

        return the_fun
    return the_decorator
