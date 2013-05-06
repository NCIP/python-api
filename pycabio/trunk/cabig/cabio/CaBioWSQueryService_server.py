#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

##################################################
# file: CaBioWSQueryService_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /usr/local/bin/cacore2py
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from CaBioWSQueryService_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
_searchRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","search"), ofwhat=[ns0.SearchQuery_Def(pname="in0", aname="_in0", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class searchRequest:
    typecode = _searchRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        in0 -- part in0
        """
        self._in0 =  kw.get("in0")
searchRequest.typecode.pyclass = searchRequest

_searchResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","searchResponse"), ofwhat=[ns1.ArrayOf_xsd_anyType_Def(pname="searchReturn", aname="_searchReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class searchResponse:
    typecode = _searchResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        searchReturn -- part searchReturn
        """
        self._searchReturn =  kw.get("searchReturn")
searchResponse.typecode.pyclass = searchResponse

_getVersionRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getVersion"), ofwhat=[], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getVersionRequest:
    typecode = _getVersionRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        """
getVersionRequest.typecode.pyclass = getVersionRequest

_getVersionResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getVersionResponse"), ofwhat=[ZSI.TC.String(pname="getVersionReturn", aname="_getVersionReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getVersionResponse:
    typecode = _getVersionResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getVersionReturn -- part getVersionReturn
        """
        self._getVersionReturn =  kw.get("getVersionReturn")
getVersionResponse.typecode.pyclass = getVersionResponse

_existRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","exist"), ofwhat=[ZSI.TC.String(pname="in0", aname="_in0", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class existRequest:
    typecode = _existRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        in0 -- part in0
        """
        self._in0 =  kw.get("in0")
existRequest.typecode.pyclass = existRequest

_existResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","existResponse"), ofwhat=[ZSI.TC.Boolean(pname="existReturn", aname="_existReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class existResponse:
    typecode = _existResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        existReturn -- part existReturn
        """
        self._existReturn =  kw.get("existReturn")
existResponse.typecode.pyclass = existResponse

_getDataObjectRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getDataObject"), ofwhat=[ZSI.TC.String(pname="in0", aname="_in0", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getDataObjectRequest:
    typecode = _getDataObjectRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        in0 -- part in0
        """
        self._in0 =  kw.get("in0")
getDataObjectRequest.typecode.pyclass = getDataObjectRequest

_getDataObjectResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getDataObjectResponse"), ofwhat=[ZSI.TC.AnyType(pname="getDataObjectReturn", aname="_getDataObjectReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getDataObjectResponse:
    typecode = _getDataObjectResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getDataObjectReturn -- part getDataObjectReturn
        """
        self._getDataObjectReturn =  kw.get("getDataObjectReturn")
getDataObjectResponse.typecode.pyclass = getDataObjectResponse

_queryRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","query"), ofwhat=[ZSI.TC.String(pname="targetClassName", aname="_targetClassName", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.AnyType(pname="criteria", aname="_criteria", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TCnumbers.Iint(pname="startIndex", aname="_startIndex", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class queryRequest:
    typecode = _queryRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        targetClassName -- part targetClassName
        criteria -- part criteria
        startIndex -- part startIndex
        """
        self._targetClassName =  kw.get("targetClassName")
        self._criteria =  kw.get("criteria")
        self._startIndex =  kw.get("startIndex")
queryRequest.typecode.pyclass = queryRequest

_queryResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","queryResponse"), ofwhat=[ns1.ArrayOf_xsd_anyType_Def(pname="queryReturn", aname="_queryReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class queryResponse:
    typecode = _queryResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        queryReturn -- part queryReturn
        """
        self._queryReturn =  kw.get("queryReturn")
queryResponse.typecode.pyclass = queryResponse

_getAssociationRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getAssociation"), ofwhat=[ZSI.TC.AnyType(pname="source", aname="_source", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.String(pname="associationName", aname="_associationName", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TCnumbers.Iint(pname="startIndex", aname="_startIndex", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getAssociationRequest:
    typecode = _getAssociationRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        source -- part source
        associationName -- part associationName
        startIndex -- part startIndex
        """
        self._source =  kw.get("source")
        self._associationName =  kw.get("associationName")
        self._startIndex =  kw.get("startIndex")
getAssociationRequest.typecode.pyclass = getAssociationRequest

_getAssociationResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getAssociationResponse"), ofwhat=[ns1.ArrayOf_xsd_anyType_Def(pname="getAssociationReturn", aname="_getAssociationReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getAssociationResponse:
    typecode = _getAssociationResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getAssociationReturn -- part getAssociationReturn
        """
        self._getAssociationReturn =  kw.get("getAssociationReturn")
getAssociationResponse.typecode.pyclass = getAssociationResponse

_getRecordsPerQueryRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getRecordsPerQuery"), ofwhat=[], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getRecordsPerQueryRequest:
    typecode = _getRecordsPerQueryRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        """
getRecordsPerQueryRequest.typecode.pyclass = getRecordsPerQueryRequest

_getRecordsPerQueryResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getRecordsPerQueryResponse"), ofwhat=[ZSI.TCnumbers.Iint(pname="getRecordsPerQueryReturn", aname="_getRecordsPerQueryReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getRecordsPerQueryResponse:
    typecode = _getRecordsPerQueryResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getRecordsPerQueryReturn -- part getRecordsPerQueryReturn
        """
        self._getRecordsPerQueryReturn =  kw.get("getRecordsPerQueryReturn")
getRecordsPerQueryResponse.typecode.pyclass = getRecordsPerQueryResponse

_getMaximumRecordsPerQueryRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getMaximumRecordsPerQuery"), ofwhat=[], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getMaximumRecordsPerQueryRequest:
    typecode = _getMaximumRecordsPerQueryRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        """
getMaximumRecordsPerQueryRequest.typecode.pyclass = getMaximumRecordsPerQueryRequest

_getMaximumRecordsPerQueryResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getMaximumRecordsPerQueryResponse"), ofwhat=[ZSI.TCnumbers.Iint(pname="getMaximumRecordsPerQueryReturn", aname="_getMaximumRecordsPerQueryReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getMaximumRecordsPerQueryResponse:
    typecode = _getMaximumRecordsPerQueryResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getMaximumRecordsPerQueryReturn -- part getMaximumRecordsPerQueryReturn
        """
        self._getMaximumRecordsPerQueryReturn =  kw.get("getMaximumRecordsPerQueryReturn")
getMaximumRecordsPerQueryResponse.typecode.pyclass = getMaximumRecordsPerQueryResponse

_getTotalNumberOfRecordsRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getTotalNumberOfRecords"), ofwhat=[ZSI.TC.String(pname="targetClassName", aname="_targetClassName", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.AnyType(pname="criteria", aname="_criteria", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getTotalNumberOfRecordsRequest:
    typecode = _getTotalNumberOfRecordsRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        targetClassName -- part targetClassName
        criteria -- part criteria
        """
        self._targetClassName =  kw.get("targetClassName")
        self._criteria =  kw.get("criteria")
getTotalNumberOfRecordsRequest.typecode.pyclass = getTotalNumberOfRecordsRequest

_getTotalNumberOfRecordsResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","getTotalNumberOfRecordsResponse"), ofwhat=[ZSI.TCnumbers.Iint(pname="getTotalNumberOfRecordsReturn", aname="_getTotalNumberOfRecordsReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class getTotalNumberOfRecordsResponse:
    typecode = _getTotalNumberOfRecordsResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        getTotalNumberOfRecordsReturn -- part getTotalNumberOfRecordsReturn
        """
        self._getTotalNumberOfRecordsReturn =  kw.get("getTotalNumberOfRecordsReturn")
getTotalNumberOfRecordsResponse.typecode.pyclass = getTotalNumberOfRecordsResponse

_queryObjectRequestTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","queryObject"), ofwhat=[ZSI.TC.String(pname="targetClassName", aname="_targetClassName", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.AnyType(pname="criteria", aname="_criteria", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class queryObjectRequest:
    typecode = _queryObjectRequestTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        targetClassName -- part targetClassName
        criteria -- part criteria
        """
        self._targetClassName =  kw.get("targetClassName")
        self._criteria =  kw.get("criteria")
queryObjectRequest.typecode.pyclass = queryObjectRequest

_queryObjectResponseTypecode = Struct(pname=("http://webservice.system.nci.nih.gov","queryObjectResponse"), ofwhat=[ns1.ArrayOf_xsd_anyType_Def(pname="queryObjectReturn", aname="_queryObjectReturn", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=None, encoded="http://webservice.system.nci.nih.gov")
class queryObjectResponse:
    typecode = _queryObjectResponseTypecode
    __metaclass__ = pyclass_type
    def __init__(self, **kw):
        """Keyword parameters:
        queryObjectReturn -- part queryObjectReturn
        """
        self._queryObjectReturn =  kw.get("queryObjectReturn")
queryObjectResponse.typecode.pyclass = queryObjectResponse


# Service Skeletons
class CaBioWSQueryService(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/cabio43/services/caBIOService', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_search(self, ps, **kw):
        request = ps.Parse(searchRequest.typecode)
        return request,searchResponse()

    soapAction[''] = 'soap_search'
    root[(searchRequest.typecode.nspname,searchRequest.typecode.pname)] = 'soap_search'

    def soap_getVersion(self, ps, **kw):
        request = ps.Parse(getVersionRequest.typecode)
        return request,getVersionResponse()

    soapAction[''] = 'soap_getVersion'
    root[(getVersionRequest.typecode.nspname,getVersionRequest.typecode.pname)] = 'soap_getVersion'

    def soap_exist(self, ps, **kw):
        request = ps.Parse(existRequest.typecode)
        return request,existResponse()

    soapAction[''] = 'soap_exist'
    root[(existRequest.typecode.nspname,existRequest.typecode.pname)] = 'soap_exist'

    def soap_getDataObject(self, ps, **kw):
        request = ps.Parse(getDataObjectRequest.typecode)
        return request,getDataObjectResponse()

    soapAction[''] = 'soap_getDataObject'
    root[(getDataObjectRequest.typecode.nspname,getDataObjectRequest.typecode.pname)] = 'soap_getDataObject'

    def soap_query(self, ps, **kw):
        request = ps.Parse(queryRequest.typecode)
        return request,queryResponse()

    soapAction[''] = 'soap_query'
    root[(queryRequest.typecode.nspname,queryRequest.typecode.pname)] = 'soap_query'

    def soap_getAssociation(self, ps, **kw):
        request = ps.Parse(getAssociationRequest.typecode)
        return request,getAssociationResponse()

    soapAction[''] = 'soap_getAssociation'
    root[(getAssociationRequest.typecode.nspname,getAssociationRequest.typecode.pname)] = 'soap_getAssociation'

    def soap_getRecordsPerQuery(self, ps, **kw):
        request = ps.Parse(getRecordsPerQueryRequest.typecode)
        return request,getRecordsPerQueryResponse()

    soapAction[''] = 'soap_getRecordsPerQuery'
    root[(getRecordsPerQueryRequest.typecode.nspname,getRecordsPerQueryRequest.typecode.pname)] = 'soap_getRecordsPerQuery'

    def soap_getMaximumRecordsPerQuery(self, ps, **kw):
        request = ps.Parse(getMaximumRecordsPerQueryRequest.typecode)
        return request,getMaximumRecordsPerQueryResponse()

    soapAction[''] = 'soap_getMaximumRecordsPerQuery'
    root[(getMaximumRecordsPerQueryRequest.typecode.nspname,getMaximumRecordsPerQueryRequest.typecode.pname)] = 'soap_getMaximumRecordsPerQuery'

    def soap_getTotalNumberOfRecords(self, ps, **kw):
        request = ps.Parse(getTotalNumberOfRecordsRequest.typecode)
        return request,getTotalNumberOfRecordsResponse()

    soapAction[''] = 'soap_getTotalNumberOfRecords'
    root[(getTotalNumberOfRecordsRequest.typecode.nspname,getTotalNumberOfRecordsRequest.typecode.pname)] = 'soap_getTotalNumberOfRecords'

    def soap_queryObject(self, ps, **kw):
        request = ps.Parse(queryObjectRequest.typecode)
        return request,queryObjectResponse()

    soapAction[''] = 'soap_queryObject'
    root[(queryObjectRequest.typecode.nspname,queryObjectRequest.typecode.pname)] = 'soap_queryObject'

