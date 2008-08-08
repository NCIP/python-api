# This API was generated by pyCaCORE
import cabig.evs.EVSWSQueryService_client as services
 
from cabig.cacore.ws.axis import AxisReader, ZSIDebugStreamReader
from cabig.cacore.ws.proxy import *

from cabig.evs.domain import *

class EVSApplicationService:

    def __init__(self, url=None, debug=False):
        locator = services.EVSWSQueryServiceLocator()
        tracefile = None
        if debug: tracefile = ZSIDebugStreamReader()
        self.wsq = locator.getevsapi41Service(url=url, 
            readerclass=AxisReader, tracefile=tracefile)
        
    def wrap(self, holder):
        try:
            (pkg, className) = holder.typecode.type
        except AttributeError:
            # not a ZSI holder type, don't try to wrap it
            return holder
        clazz = globals()[className]
        return clazz(holder,self)
        
    def queryObject(self, targetClassName, criteria):
        q = services.queryObjectRequest()
        q._targetClassName = targetClassName
        q._criteria = criteria.holder
        v = self.wsq.queryObject(q)
        return [self.wrap(i) for i in v.QueryObjectReturn.Item]
    
