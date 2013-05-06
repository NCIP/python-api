#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

# The location of the input WSDL
WSDL_FILE = "conf/cabio43.wsdl"

# Root package for the resulting API 
ROOT_PACKAGE = "cabig.cabio"

# Mapping from Java to Python packages 
# The ROOT_PACKAGE is prepended to each Python package
PACKAGE_MAPPING = {
    'gov.nih.nci.cabio.domain' : 'domain',
    'gov.nih.nci.cabio.pathways' : 'pathways',
    'gov.nih.nci.common.domain' : 'common.domain',
    'gov.nih.nci.common.provenance.domain' : 'common.provenance.domain',
}

SERVICE_CLASS_NAME = "CaBioApplicationService"

OUTPUT_DIR = "output"
