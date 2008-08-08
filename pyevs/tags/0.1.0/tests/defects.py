import unittest
from cabig.evs.service import *

class DefectsTest(unittest.TestCase):
    """ These tests are expected to fail until the defects are fixed, at which 
        point they will be moved to another test suite. 
    """ 
  
    def setUp(self):
        self.es = EVSApplicationService()
    
    def testGetAssociation(self):
        ''' This is actually a defect in the EVS WS API, in that it doesn't 
            support the getAssociation method which should be standard
            on caCORE-like web services.
        '''
        
        s = EVSApplicationService()
        d = DescLogicConcept(name='intronic')
        results = s.queryObject(d.className, d)

        self.failUnless(results)
        
        # will fail with "This service does not support the getAssociation method."
        results[0].propertyCollection
        
    
if __name__ == '__main__':
    unittest.main()
