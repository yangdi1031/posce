'''
Tests for 'posce.comms.edit'.
'''

import subprocess

import click

from posce.comms.edit           import edit
from tests.test_items.test_book import book
from tests.tools                import out

def test_edit(book, monkeypatch):
    # setup
    args = {}
    func = lambda a, **k: args.update({'args': a, **k})
    monkeypatch.setattr(subprocess, 'run', func)

    # success: defaults
    assert out(book, edit, 'alpha') == []
    assert args == {
        'args':  [book['alpha'].path],
        'shell': True,
    }

    # success: --editor
    assert out(book, edit, 'alpha', '-e', 'test') == []
    assert args == {
        'args':  ['test', book['alpha'].path],
        'shell': True,
    }
