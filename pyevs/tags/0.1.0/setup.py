#!/usr/bin/env python

from setuptools import setup

setup(name='pyEVS',
      version='0.1.0',
      description='EVS Python API',
      long_description='Pythonic API for caCORE EVS API based on web services',
      license='caBIG Open Source Software License',
      platforms='All',
      author='Konrad Rokicki',
      author_email='rokickik@mail.nih.gov',
      url='http://evsapi.nci.nih.gov/',
      packages=[
            'cabig',
            'cabig.evs',
      ],
      install_requires=['pyCaCORE==0.1.0'],
      namespace_packages = ['cabig'],
      dependency_links = [
            'https://gforge.nci.nih.gov/frs/download.php/4256/pyCaCORE-0.1.0-py2.5.egg'
      ],
      test_suite = 'tests.unit_tests'
     )
