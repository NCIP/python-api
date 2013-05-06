#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

import unittest
from cabig.evs.service import *

class WSTest(unittest.TestCase):
    
    def setUp(self):
        self.es = EVSApplicationService()

    def testDescLogicConcept(self):
    
        s = EVSApplicationService()
        d = DescLogicConcept(name='blood')
        results = self.es.queryObject(d.className, d)
        
        self.failUnless(results)
        self.failUnless(results[0].name)
        self.failUnless(results[0].code)
        self.failUnless(len(results) >= 3)
    
        
    def testPropertiesForConcept(self):
        """ This is sort of a work-around to the EVS web service missing 
            getAssociation. Instead of getting a DescLogicConcept and then 
            calling d.propertyCollection, we just use Property as our target 
            object.
        """
        s = EVSApplicationService()
        d = DescLogicConcept(code='C13249') # "intronic"
        results = self.es.queryObject(Property.className, d)
        
        # This will lose some information since dictionaries can't have duplicate keys!
        props = dict([(p.name,p.value) for p in results]) 
        
        self.failUnless('DEFINITION' in props)
        self.failUnless('CONCEPT_NAME' in props)
        self.failUnless('UMLS_CUI' in props)
        self.failUnless('Preferred_Name' in props)
        self.failUnless('Semantic_Type' in props)
        self.failUnless('FULL_SYN' in props)
        
        
    def testMetaThesaurus(self):
        """ Metathesaurus concepts come with synonyms preloaded. We can access
            preloaded associations even without getAssociation. 
        """
        m = MetaThesaurusConcept(name='NCBI')
        results = self.es.queryObject(MetaThesaurusConcept.className, m)
        self.failUnless(results[0].name)
        self.failUnless(results[0].cui)
        self.failUnless(results[0].synonymCollection)
        
    
    def testAtoms(self):
        """ Test getting stuff from atoms. Again, we have to use target object
            since there is no getAssociation method.
        """
        m = MetaThesaurusConcept(name='NCBI')
        results = self.es.queryObject(Atom.className, m)
        self.assertEquals(results[0].source.abbreviation, results[0].origin)
        
        
if __name__ == '__main__':
    unittest.main()
