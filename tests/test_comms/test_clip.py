'''
Tests for 'posce.comms.clip'.
'''

import pyperclip

from posce.comms.clip           import clip
from tests.test_items.test_book import book
from tests.tools                import out

def test_clip(book, monkeypatch):
    # setup
    args = []
    monkeypatch.setattr(pyperclip, 'copy', lambda *a: args.extend(a))

    # success: defaults
    assert out(book, clip, 'alpha') == []
    assert args == ['alpha']
