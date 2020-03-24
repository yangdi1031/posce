'''
Tests for 'posce.comms.edit'.
'''

import click

from posce.comms.edit           import edit
from tests.test_items.test_book import book
from tests.tools                import out

def test_edit(book, monkeypatch):
    # setup
    args = {}
    monkeypatch.setattr(click, 'edit', lambda **k: args.update(k))

    # success: defaults
    assert out(book, edit, 'alpha') == []
    assert args == {
        'editor':    None,
        'extension': '.txt',
        'filename':  book['alpha'].path,
    }

    # success: --editor
    assert out(book, edit, 'alpha', '-e', 'test') == []
    assert args == {
        'editor':    'test',
        'extension': '.txt',
        'filename':  book['alpha'].path,
    }
