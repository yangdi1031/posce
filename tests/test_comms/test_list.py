'''
Tests for 'posce.comms.list'.
'''

import time

from posce.comms.list           import list
from tests.test_items.test_book import book
from tests.tools                import out

def test_list(book):
    # success: defaults
    assert out(book, list) == [
        'alpha\n',
        'bravo\n',
        'charlie\n',
    ]

    # success: GLOB
    assert out(book, list, 'a*') == [
        'alpha\n',
    ]

    # success: --reverse --sort size
    assert out(book, list, '-r', '-s', 'size') == [
        'charlie\n',
        'bravo\n',
        'alpha\n',
    ]

    # success: --sort time
    book['bravo'].time   = time.localtime(time.time() + 1)
    book['charlie'].time = time.localtime(time.time() + 2)
    book['alpha'].time   = time.localtime(time.time() + 3)
    assert out(book, list, '-s', 'time') == [
        'bravo\n',
        'charlie\n',
        'alpha\n',
    ]
