# -*- coding: utf-8 -*-
#
# Copyright 2016 Daisuke Miyakawa
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup, find_packages

setup(name='pybin_exp',
      version='0.1',
      author='Daisuke Miyakawa',
      author_email='dev.null@mowa-net.jp',
      description='PyBin Experiment',
      long_description='No README',
      packages=find_packages(),
      license='Apache License 2.0',
      entry_points={
          'console_scripts': ['pybin = pybin.main:main']
      },
      url='https://github.com/dmiyakawa/pybin_exp',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Markup'])
