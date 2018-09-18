from configurator import Config
from .cfgctx import CFGCTX

@Config("foo", "foo value", default='foo', arg_name='cfg', context=CFGCTX)
def foo(*,cfg=None):
    return cfg
