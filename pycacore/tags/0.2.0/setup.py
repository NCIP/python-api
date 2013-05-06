#!/usr/bin/env python

#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

from setuptools import setup

setup(name='pyCaCORE',
      version='0.1.0',
      description='caCORE Python API Generator',
      long_description='Python API generator for caCORE-like systems',
      license='caBIO Software License',
      platforms='All',
      author='Konrad Rokicki',
      author_email='rokickik@mail.nih.gov',
      url='http://cabioapi.nci.nih.gov/',
      packages=[
            'cabig',
            'cabig.cacore',
            'cabig.cacore.generate',
            'cabig.cacore.ws',
      ],
      include_package_data = True,
      namespace_packages = ['cabig'],
      install_requires = [ "setuptools >= 0.6c3", 'ZSI==2.1_a1' ],
      dependency_links = [
            'http://downloads.sourceforge.net/pywebsvcs/ZSI-2.1_a1-py2.5.egg',
      ],
      entry_points = {
            'console_scripts': [
            'cacore2py = cabig.cacore.generate.commands:cacore2py',
         ],
      },
)
