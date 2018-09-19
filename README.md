# configurator

A simple configuration injector based on configparser using function decorators and keyword arguments.

In fact the idea is so simple and straight forward, that I believe someone has written something like that before.


## Installation




## Example


From `examples/greeter.py`:

```python
import sys, os, tempfile
from configurator import Config, read_config_file


@Config('greeter','greeting', default='Hello,')
def greet(name='World', *, greeting):
    print(f"{greeting} {name}")


@Config('greeter', 'farewell', default='Good bye,')
def farewell(name='World', *, farewell):
    print(f"{farewell} {name}")


if __name__ == '__main__':
    tmp = tempfile.mktemp()
    print(f'Writing default config to and reading from: {tmp}')
    read_config_file(tmp)

    greet()
    farewell()

    if not '-k' in sys.argv:
        os.unlink(tmp)
    else:
        print('Keeping temp file.')
```
