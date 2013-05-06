#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

from cabig.evs.service import *
s = EVSApplicationService()

print "Search meta thesaurus for 'NCBI'"
print

m = MetaThesaurusConcept(name='NCBI')
results = s.queryObject(MetaThesaurusConcept.className, m)
for r in results:
    print r.cui, r.name
    print "Synonyms:",', '.join(r.synonymCollection)
    print

print "Search for 'intronic' properties"
print

d = DescLogicConcept(name='intronic')
results = s.queryObject(Property.className, d)
for p in results:
    print "%s: %s" % (p.name, p.value)


