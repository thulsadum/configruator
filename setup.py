from setuptools import setup

setup(
    name='configurator',
    version='0.1.0',
    packages=['tests', 'tests.test_advanced'],
    url='https://github.com/thulsadum/configruator',
    license='MIT',
    author='Sebastian Claus',
    author_email='sbstncls@gmail.com',
    description='A simple configuration injector based on configparser using function decorators and keyword arguments.'
)
