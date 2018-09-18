from configurator import Config
from .cfgctx import CFGCTX

@Config("bar", "bar value", default='bar', arg_name='cfg', context=CFGCTX)
def bar(*,cfg=None):
    return cfg
