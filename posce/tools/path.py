'''
Filepath string manipulation functions.
'''

import os.path

EXPANSIONS = {
    '%': os.path.expandvars,
    '~': os.path.expanduser,
    '$': os.path.expandvars,
}

def strpath(func):
    '''
    Decorate a function to cast the first argument to a string.
    '''

    def deco(path, *args, **kwargs):
        return func(str(path), *args, **kwargs)
    return deco

@strpath
def base(path):
    '''
    Return a path's basename with the extension.
    '''

    return os.path.basename(path)

@strpath
def clean(path):
    '''
    Return a normalised path.
    '''

    return os.path.normpath(path)

@strpath
def expand(path):
    '''
    Return a clean variable-expanded path.
    '''

    for char, func in EXPANSIONS.items():
        if char in path:
            path = func(path)
    return path

@strpath
def ext(path):
    '''
    Return a path's extension without a dot.
    '''

    part = os.path.splitext(path)
    return part[-1].lstrip('.')

def join(*elems):
    '''
    Return a clean joined filepath.
    '''

    elems = map(str, elems)
    return os.path.normpath(os.path.join(*elems))

@strpath
def name(path):
    '''
    Return a path's basename without the extension.
    '''

    base = os.path.basename(path)
    return os.path.splitext(base)[0]

@strpath
def parent(path):
    '''
    Return a path's parent directory.
    '''

    return os.path.normpath(os.path.dirname(path))
