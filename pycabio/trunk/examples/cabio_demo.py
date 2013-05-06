#!/usr/bin/env python

#L
# Copyright SAIC
#
# Distributed under the OSI-approved BSD 3-Clause License.
# See http://ncip.github.com/python-api/LICENSE.txt for details.
#L

#
# Basic example which retrieves some genes and prints information about them.
#

from cabig.cabio.service import *

c = CaBioApplicationService()

gene = Gene()
gene.symbol = 'brca*'

r = c.queryObject(Gene.className, gene)

for g in r:
    print "%s (%s) - %s" % (g.symbol,g.taxon.commonName,g.fullName)
    for x in g.databaseCrossReferenceCollection:
        print "    %s: %s" % (x.dataSourceName, x.crossReferenceId)

