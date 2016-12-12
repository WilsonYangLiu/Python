rm(list = ls())
setwd(dir = "/home/wilson/Dropbox/Document/keggapi/")
if(!require("data.table")){
  install.packages("data.table")
  library("data.table")
}

gene_hsa <- read.table(file = "gene_hsa.txt", sep = '\t', quote = "", dec = "\n", 
                       col.names = c("kGeneID", "description"))
pathway_hsa <- read.table(file = "pthway_hsa.txt", sep = '\t', quote = "", dec = "\n",
                         col.names = c("pathway", "description"))
NCBI_GeneID2KEGG_ID <- read.table(file = "NCBI GeneID - KEGG ID.txt", sep = '\t', 
                                  quote = "", dec = "\n", 
                                  col.names = c("NCBI_GeneID", "kGeneID"))
pathway2hsaGene <- read.table(file = "link_pathway-hsaGene.txt", sep = '\t', 
                              quote = "", dec = "\n", 
                              col.names = c("pathway", "kGeneID"))
#save(gene_hsa, pathway_hsa, NCBI_GeneID2KEGG_ID, pathway2hsaGene, file = "hsa.Rdata")

load(file = "hsa.Rdata")

gene_hsa <- data.table(gene_hsa)
setkey(gene_hsa, kGeneID)

NCBI_GeneID2KEGG_ID <- data.table(NCBI_GeneID2KEGG_ID)
NCBI_GeneID2KEGG_ID$NCBI_GeneID <- gsub("ncbi-geneid:","",NCBI_GeneID2KEGG_ID$NCBI_GeneID)
setkey(NCBI_GeneID2KEGG_ID, kGeneID)

entrzid <- NCBI_GeneID2KEGG_ID[gene_hsa, nomatch=NA, mult="all"]

pathway_hsa <- data.table(pathway_hsa)
pathway_hsa$pathway <- gsub("path:", "", pathway_hsa$pathway)
setkey(pathway_hsa, pathway)

pathway2hsaGene <- data.table(pathway2hsaGene)
pathway2hsaGene$pathway <- gsub("path:", "", pathway2hsaGene$pathway)
setkey(pathway2hsaGene, pathway)

a <- (pathway2hsaGene[pathway_hsa, nomatch=NA, mult="all"])
setkey(a, kGeneID)
#key(a) == key(entrzid)
#uniqueID <- as.character(unique(a$kGeneID))
uniqueID <- intersect(as.character(a$kGeneID), as.character(entrzid$kGeneID))
aa <- entrzid[uniqueID,]

pathway <- a[aa, nomatch=NA, mult="all"]
setkey(pathway, pathway)

pathway <- data.table(Pathway=paste(pathway$pathway, pathway$description, sep = ": "), 
                      Entrzid=pathway$NCBI_GeneID, KGeneID=pathway$kGeneID, 
                      GeneTerm=pathway$i.description)
setkey(pathway, Pathway)

#save(entrzid, pathway, file = "hsa-Integrate.Rdata")
load(file = "hsa-Integrate.Rdata")

uniquePath <- as.character(unique(pathway$Pathway))
for (i in 1:length(uniquePath)) {
  path <- pathway[uniquePath[i]]
  write.table(x = as.character(path$Entrzid), file = substring(uniquePath[i], 1, 8), 
              quote = FALSE, row.names = FALSE, col.names = FALSE)
}



