
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
