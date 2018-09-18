from unittest import TestCase, main
from tempfile import TemporaryDirectory
from pathlib import Path
from configparser import ConfigParser

from configurator import write_default_config
from tests.test_advanced.cfgctx import CFGCTX

from tests.test_advanced.foo import foo
from tests.test_advanced.bar import bar


class AdvancedTC(TestCase):

    def test_foo(self):
        self.assertEqual(CFGCTX.default_config.get('foo', 'foo value'), 'foo', 'default value')
        self.assertEqual(CFGCTX.config.get('foo', 'foo value'), 'foo', 'config value')
        self.assertEqual(foo(), 'foo', 'method call')

    def test_bar(self):
        self.assertEqual(CFGCTX.default_config.get('bar', 'bar value'), 'bar', 'default value')
        self.assertEqual(CFGCTX.config.get('bar', 'bar value'), 'bar', 'config value')
        self.assertEqual(bar(), 'bar', 'method call')

    def test_write_defaults(self):
        with TemporaryDirectory() as tdir:
            tfile = Path(tdir) / 'configfile'
            with open(tfile, 'w') as fp:
                write_default_config(fp, context=CFGCTX)

            cfg = ConfigParser()
            with open(tfile, 'r') as fp:
                cfg.read_file(fp, tfile)

            self.assertEqual(cfg['foo']['foo value'],'foo', 'foo read from file')
            self.assertEqual(cfg['bar']['bar value'],'bar', 'bar read from file')


if __name__ == '__main__':
    main()
