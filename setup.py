#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, find_packages


with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy >= 1.12.0',
    'six >= 1.10.0',
    'protobuf >= 3.4.0',
    'tornado',
    'html5lib == 0.9999999',  # identical to 1.0b8
    'markdown >= 2.6.8',
    'bleach == 1.5.0',

    # futures is a backport of the concurrent.futures module added in
    # python 3.2
    'futures >= 3.1.1;python_version < "3.2"',
    # python3 specifically requires wheel 0.26
    'wheel;python_version < "3"',
    'wheel >= 0.26;python_version >= "3"',
]

test_requirements = [
    'pytest',
]

CONSOLE_SCRIPTS = [
    'trainboard = trainboard.main:run_main',
]

setup(
    name='trainboard',
    version='1.0',
    description='Deep Learning Trainboard for in your browser',
    long_description= history,
    author='TAIR.AI',
    author_email='nasa@nos.ai',
    url='https://github.com/tair-ai/trainboard',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    package_data={
        'trainboard': [
            'webfiles.zip',
        ],
    },
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

# python setup.py sdist bdist_wheel --universal upload
# twine upload dist/*
