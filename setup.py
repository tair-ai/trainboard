#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'protobuf >= 0.3.2',
    'six',
]

test_requirements = [
    'pytest',
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
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
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
