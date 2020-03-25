'''
PyPi setup script.
'''

from setuptools import find_packages, setup

from posce import VERSION_NUMBER

DEPENDENCIES = [
    'click>=7.1.1',
    'pyperclip>=1.7.0',
    'Send2Trash>=1.5.0',
]

setup(
    # Basic information.
    name         = 'posce',
    version      = VERSION_NUMBER,
    keywords     = 'cli notes note-taking',
    description  = 'A note-taking toolkit for your command line.',
    url          = 'https://github.com/posce/posce',
    author       = 'Stephen Malone',
    author_email = 'mail@posce.org',

    # Project description.
    long_description = open('readme.md').read(),
    long_description_content_type = 'text/markdown',

    # Package specifications.
    packages         = find_packages(exclude=['*tests*']),
    python_requires  = '>=3.8.0',
    install_requires = DEPENDENCIES,

    # Console executables.
    entry_points = {
        'console_scripts': ['posce=posce.__main__:main'],
    },

    # Project URLs.
    project_urls = {
        'Homepage': 'https://github.com/posce/posce',
        'Issues':   'https://github.com/posce/posce/issues',
    },

    # Project classifiers.
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business',
    ],
)
