##change _<PA> in file name for different road networks
import networkx as nx
import operator
import csv

g=nx.read_weighted_edgelist("weighted_roadNet_PA.txt")
rank=nx.pagerank(g);
sortedrank= sorted(rank.items(),key=operator.itemgetter(1))
reverse=sortedrank[::-1]
topnodes=reverse[:20]
print topnodes

filewrite=open("pagerankPA.csv",'wb')
wr= csv.writer(filewrite,dialect='excel')
for item in reverse:
	wr.writerow(item)

h,a = nx.hits(g,tol=1e-02)
sortedhits=sorted(h.items(),key=operator.itemgetter(1))
sortedauth=sorted(a.items(),key=operator.itemgetter(1))
reversehits=sortedhits[::-1]
reverseauth=sortedauth[::-1]

print reversehits[:20]
print reverseauth[:20]

filewrite=open("hitsPA.csv",'wb')
wr= csv.writer(filewrite,dialect='excel')
for item in reversehits:
	wr.writerow(item)

filewrite=open("authPA.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in reverseauth:
	wr.writerow(item)
