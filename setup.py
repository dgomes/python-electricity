#  python-electricity
#  ---------------
#  Python library for identitying the tariff period of a given date. 
#
#  Author:  Diogo Gomes <diogogomes@gmail.com> (c) 2019
#  Website: https://github.com/dgomes/python-electricity
#  License: MIT (see LICENSE file)

import codecs
import re
import io
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with codecs.open('electricity/tariffs.py', 'r', 'utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

try:
    with io.open(os.path.join(".", 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    raise RuntimeError('Cannot find README.md')

setup(
    name='python-electricity',
    version=version,
    packages=find_packages(),
    author='dgomes',
    author_email='diogogomes@gmail.com',
    maintainer='dgomes',
    maintainer_email='diogogomes@gmail.com',
    url='https://github.com/dgomes/python-electricity',
    bugtrack_url='https://github.com/dgomes/python-electricity/issues',
    license='MIT',
    py_modules=['electricity'],
    description='Determine Electricity Tariff Periods in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)
