'''
Tests for 'posce.comms.drop'.
'''

import send2trash

from posce.comms.drop           import drop
from tests.test_items.test_book import book
from tests.tools                import out

def test_copy(book, monkeypatch):
    # setup
    args = []
    monkeypatch.setattr(send2trash, 'send2trash', lambda *a: args.extend(a))

    # success: defaults
    assert out(book, drop, 'alpha') == []
    assert args == [book['alpha'].path]
