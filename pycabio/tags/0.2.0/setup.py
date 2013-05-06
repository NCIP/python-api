#!/usr/bin/env python

#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

from setuptools import setup

setup(name='pyCaBio',
      version='0.2.0',
      description='caBIO Python API',
      long_description='Pythonic API for the caBIO Database based on web services',
      license='caBIG Open Source Software License',
      platforms='All',
      author='Konrad Rokicki',
      author_email='rokickik@mail.nih.gov',
      url='http://cabioapi.nci.nih.gov/',
      packages=[
            'cabig',
            'cabig.cabio',
            'cabig.cabio.common',
            'cabig.cabio.common.provenance',
      ],
      install_requires=['pyCaCORE==0.1.0'],
      namespace_packages = ['cabig'],
      dependency_links = [
            'https://gforge.nci.nih.gov/frs/download.php/4256/pyCaCORE-0.1.0-py2.5.egg'
      ],
      test_suite = 'tests.unit_tests'
     )
