"""
TODO: Implement write functions.

Implement chunked files objects
"""
import locale

ENCODE = locale.getpreferredencoding()
ERROR = 'strict'


def _read(path, mode, encode, error):
    with open(path, mode, encoding=encode, errors=error) as file:
        return file


def read(path: str):
    return _read(path, 'r', ENCODE, ERROR).read()


def readb(path: str):
    return _read(path, 'rb', None, None).read()


def readi(path: str, mode='r'):
    if mode == 'rb':
        return _read(path, mode, None, None).readlines()
    return _read(path, 'r', ENCODE, ERROR).readlines()
