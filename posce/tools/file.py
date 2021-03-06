'''
File I/O and discovery functions.
'''

import glob
import os
import shutil
import time

from posce.tools.path import strpath

OPTIONS = {
    'encoding': 'utf-8',
}

@strpath
def append(path, string, *, sep='\n'):
    '''
    Append a string to a file.
    '''

    with open(path, 'a', **OPTIONS) as file:
        file.write(sep + string)

@strpath
def copy(path, name):
    '''
    Copy a file to another name in the same directory.
    '''

    dire = os.path.dirname(path)
    ext  = os.path.splitext(path)[-1]
    dest = os.path.join(dire, name + ext)
    shutil.copyfile(path, dest)

@strpath
def create(path, string):
    '''
    Write a string to a new file.
    '''

    with open(path, 'x', **OPTIONS) as file:
        file.write(string)

@strpath
def exists(path):
    '''
    Return true if a file or directory exists.
    '''

    return os.path.exists(path)

@strpath
def find(dire, term):
    '''
    Yield all files in a directory with names matching a glob pattern.
    '''

    pattern = os.path.normpath(os.path.join(dire, term))
    yield from glob.iglob(pattern)

@strpath
def mtime(path):
    '''
    Return a file's modification time as a time struct.
    '''

    try:
        secs = os.path.getmtime(path)
        return time.localtime(secs)
    except:
        return None

@strpath
def read(path):
    '''
    Return the contents of a file as a string.
    '''

    with open(path, 'r', **OPTIONS) as file:
        return file.read()

@strpath
def reext(path, ext):
    '''
    Move a file to a different extension in the same directory.
    '''

    dire = os.path.dirname(path)
    name = os.path.splitext(os.path.basename(path))[0]
    dest = os.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)

@strpath
def rename(path, name):
    '''
    Move a file to a different name in the same directory.
    '''

    dire = os.path.dirname(path)
    ext  = os.path.splitext(path)[-1].lstrip('.')
    dest = os.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)

@strpath
def size(path):
    '''
    Return a file's size in bytes.
    '''

    try:
        return os.path.getsize(path)
    except:
        return None

@strpath
def write(path, string):
    '''
    Write a string to a file.
    '''

    with open(path, 'w', **OPTIONS) as file:
        file.write(string)
