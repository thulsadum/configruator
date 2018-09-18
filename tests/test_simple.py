from unittest import TestCase, main
from tempfile import TemporaryDirectory
from pathlib import Path
from configparser import ConfigParser

from configurator import Config, write_default_config, get_default_context


@Config("foo", "foo value", default='foo', arg_name='cfg')
def foo(*,cfg=None):
    return cfg


@Config("bar", "bar value", default='bar', arg_name='cfg')
def bar(*,cfg=None):
    return cfg


class SimpleTC(TestCase):

    def test_foo(self):
        self.assertEqual(get_default_context().default_config.get('foo', 'foo value'), 'foo', 'default value')
        self.assertEqual(get_default_context().config.get('foo', 'foo value'), 'foo', 'config value')
        self.assertEqual(foo(), 'foo', 'method call')

    def test_bar(self):
        self.assertEqual(get_default_context().default_config.get('bar', 'bar value'), 'bar', 'default value')
        self.assertEqual(get_default_context().config.get('bar', 'bar value'), 'bar', 'config value')
        self.assertEqual(bar(), 'bar', 'method call')

    def test_write_defaults(self):
        with TemporaryDirectory() as tdir:
            tfile = Path(tdir) / 'configfile'
            with open(tfile, 'w') as fp:
                write_default_config(fp)

            cfg = ConfigParser()
            with open(tfile, 'r') as fp:
                cfg.read_file(fp, tfile)

            self.assertEqual(cfg['foo']['foo value'],'foo', 'foo read from file')
            self.assertEqual(cfg['bar']['bar value'],'bar', 'bar read from file')


if __name__ == '__main__':
    main()
