# -*- coding: utf-8 -*-
## This file is part of hawck.
##
## hawck is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## hawck is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with hawck.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='hawck',
      version=version,
      description="Simple tasks manager",
      long_description=open("README.rst").read(),
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: X11 Applications :: GTK',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Topic :: Utilities',
                   ],
      keywords='',
      author='Felipe Reyes',
      author_email='freyes@tty.cl',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points= {"console_scripts":
                     ['hawck = hawck:start',],
                     }
      )
