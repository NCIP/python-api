#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

# The location of the input WSDL
# http://evsapi.nci.nih.gov/evsapi41/services/evsapi41Service?wsdl
WSDL_FILE = "conf/evsapi41.wsdl"

# Root package for the resulting API 
ROOT_PACKAGE = "cabig.evs"

# Mapping from Java to Python packages 
# The ROOT_PACKAGE is prepended to each Python package
PACKAGE_MAPPING = {
    'gov.nih.nci.evs.domain' : 'domain',
}

SERVICE_CLASS_NAME = "EVSApplicationService"

OUTPUT_DIR = "output"
