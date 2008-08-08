# This API was generated by pyCaCORE
import cabig.cabio.CaBioWSQueryService_client as services
from cabig.cacore.ws.proxy import *

schema = services.ns5

class DatabaseCrossReference(WSBean):

    arrayType =  services.ns1.ArrayOf_xsd_anyType_Def(None).pyclass
    className = "gov.nih.nci.common.domain.DatabaseCrossReference"

    crossReferenceId = ProxyAttr('crossReferenceId')
    dataSourceName = ProxyAttr('dataSourceName')
    id = ProxyAttr('id')
    sourceType = ProxyAttr('sourceType')
    summary = ProxyAttr('summary')
    type = ProxyAttr('type')
    SNP = ProxyAssoc('SNP',False)
    gene = ProxyAssoc('gene',False)
    nucleicAcidSequence = ProxyAssoc('nucleicAcidSequence',False)
    
    def __init__(self, holder=None, service=None, **kwargs):
        if not(holder): holder = schema.DatabaseCrossReference_Def(None).pyclass()
        WSBean.__init__(self, holder, service=service, **kwargs)
    
