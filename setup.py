#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='tax-calculator',
    version='0.0.0',
    packages=find_packages('src', exclude='tests'),
    package_dir={'': 'src'},
    description='A command line tax calculator',
    long_description=README,
    author='Matthew Power',
    author_email='matthew@mthpower.uk',
    license='MIT',
    zip_safe=True,
    install_requires=[
        'click',
        'py-moneyed',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'tax-calc = tax_calculator.calc:cli',
        ],
    },
)
