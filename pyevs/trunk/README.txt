==============================
pyEVS - Python API for EVS
==============================

The EVS API allows access to NCICB's Enterprise Vocabulary Services. 

For more information about caBIO see http://evsapi.nci.nih.gov

Prerequisites
-------------
Python 2.5 

Latest setuptools
  To install, download and execute the following script:
  http://peak.telecommunity.com/dist/ez_setup.py

The installation uses setuptools to automatically install any 
other dependencies.


Installation
------------
System-wide install:

    python setup.py install

Single user install:

    python setup.py install --home=~

After installation the test suite may be run:
     
    python setup.py test

There is also example code available under the examples/ directory.


Mailing List
------------
https://list.nih.gov/archives/ncievs-l.html


Known Issues
------------
* Sending arrays (collections) is not possible due to a conflict between AXIS 
  and ZSI. See tests/defects.py for an example.
  

Change History
--------------
0.1.0 - 06/27/2008
Generated with pyCaCORE 0.1.0.
Initial alpha release
