#! python 2.7
# -*- coding: cp936 -*-
# learn from thr kegg api: http://www.kegg.jp/kegg/rest/keggapi.html

import urllib2

# operation: info
# http://rest.kegg.jp/info/<database>; <database> = pathway | genomes | genes ...
# http://rest.kegg.jp/info/<org>; <org> = hsa | ece ...
url = 'http://rest.kegg.jp/info/'
print urllib2.urlopen(url + "pathway", timeout=20).read()
print urllib2.urlopen(url + "hsa", timeout=20).read()

# operation: list ( returns a list of entry identifiers and associated definition
#                  for a given database or a given set of database entries )
# http://rest.kegg.jp/list/<database>; <database> = pathway | genomes | genes ...
# http://rest.kegg.jp/list/<org>; <org> = hsa | ece ...
# http://rest.kegg.jp/list/<database>/<org>; <database> = pathway | module, <org> = hsa | ece ...
# http://rest.kegg.jp/list/<dbentries>; <dbentry> = <db:entry> | <kid> | <org:gene>
# http://rest.kegg.jp/list/list/organism; "organism" only for list
url = 'http://rest.kegg.jp/list/'
data = urllib2.urlopen(url + "pathway", timeout=20).read()
data = urllib2.urlopen(url + "hsa", timeout=20).read()  # returns the entire list of human genes 
data = urllib2.urlopen(url + "pathway/hsa", timeout=20).read()
data = urllib2.urlopen(url + "hsa:10458+ece:Z5100", timeout=20).read()
data = urllib2.urlopen(url + "organism", timeout=20).read()

'''
name = "./gene_hsa.txt"
with open(name, "w") as txtfile:
    txtfile.write(data)
'''

# operation: find
# http://rest.kegg.jp/find/<database>/<query>; <database> = pathway | genomes | genes ...
# http://rest.kegg.jp/list/<org>/<query>; <org> = hsa | ece ...
# http://rest.kegg.jp/find/<database>/<query>/<option>; <database> = compound | drug,
#                                                       <option> = formula | exact_mass | mol_weight
url = 'http://rest.kegg.jp/find/'
data = urllib2.urlopen(url + "genes/shiga+toxin", timeout=20).read()
#data = urllib2.urlopen(url + "genes/\"shiga toxin\"", timeout=20).read()
data = urllib2.urlopen(url + "compound/C7H10O5/formula", timeout=20).read()

# operation: get
# http://rest.kegg.jp/get/<dbentries>[/<option>]; <dbentry> = <db:entry> | <kid> | <org:gene>
url = 'http://rest.kegg.jp/get/'
data = urllib2.urlopen(url + "hsa:10458+ece:Z5100", timeout=20).read()
data = urllib2.urlopen(url + "hsa05130/image", timeout=20).read()   # image obj

# operation: conv – convert KEGG identifiers to/from outside identifiers
# http://rest.kegg.jp/conv/<target_db>/<source_db>; (<target_db> <source_db>) = (<kegg_db> <outside_db>) | (<outside_db> <kegg_db>)
#                                                   <kegg_db> = <org>; drug | compound | glycan; pubchem | chebi
#                                                   <outside_db> = ncbi-proteinid | ncbi-geneid | uniprot
# http://rest.kegg.jp/conv/<target_db>/<dbentries>; <dbentry> = <db:entry> | <kid> | <org:gene>
#                                                   database entries involving the following <database>
#                                                   <database> = <org> | genes | ncbi-proteinid | ncbi-geneid | uniprot; drug | compound | glycan | pubchem | chebi
url = 'http://rest.kegg.jp/conv/'
data = urllib2.urlopen(url + "hsa/ncbi-geneid", timeout=20).read()
data = urllib2.urlopen(url + "ncbi-proteinid/hsa:10458+ece:Z5100", timeout=20).read()

'''
name = "./NCBI GeneID - KEGG ID.txt"
with open(name, "w") as txtfile:
    txtfile.write(data)
'''

# operation: link - find related entries by using database cross-references
# http://rest.kegg.jp/link/<target_db>/<source_db>; <database> = pathway | genome | <org> ...
# http://rest.kegg.jp/link/<target_db>/<dbentries>; <dbentry> = <db:entry> | <kid> | <org:gene>
url = 'http://rest.kegg.jp/link/'
data = urllib2.urlopen(url + "hsa/pathway", timeout=20).read()
data = urllib2.urlopen(url + "pathway/hsa:10458+ece:Z5100", timeout=20).read()

'''
name = "./link_pathway-hsaGene.txt"
with open(name, "w") as txtfile:
    txtfile.write(data)
'''

