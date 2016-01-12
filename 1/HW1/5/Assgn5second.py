import networkx as nx
import numpy as np
from sets import Set
import itertools


entries=np.zeros((9000000, 4),dtype=np.uint64)
count=0
node=Set([]);

graph=nx.Graph()
print "reading"
with open('activities-portland-1-v1.dat','r') as f:
    for line in f:
        
##        if count==100:
##              break;
        line= line.strip('\n')
        val=line.split(" ")
        entries[count,2]=int((val[4]))#startime
        entries[count,3]=((val[4]+val[5]))#endtime
        entries[count,0]=((val[1]))#id
        entries[count,1]=((val[6]))#location
        count=count+1
        node.add(val[1])
        #graph.add_node(val[1])

#print entries
print "sorting"

entries=sorted(entries, key=lambda entries_entry: entries_entry[1])
#print entries
print "procesing"
sublist=list()
for i in range(0,len(entries)-1):

    if i%10000==0:
        print i;
    if entries[i][1]==entries[i+1][1]:
        sublist.append(entries[i].tolist())
    else:
        sublist.append(entries[i].tolist())
        #print sublist
        if len(sublist)>1:
            value=set()
            for pair in itertools.combinations(sublist,2):
                if pair[0][0]!=pair[1][0]:
                    if ((pair[0][0],pair[1][0]) in value)or((pair[1][0],pair[0][0]) in value):
                        n=1
                    else:
                        stime1=pair[0][2]
                        etime1=pair[0][3]
                        stime2=pair[1][2]
                        etime2=pair[1][3]
                        if (min(etime1,etime2)-max(stime1,stime2))>7200:
                            graph.add_edge(pair[0][0],pair[1][0])
                            value.add((pair[0][0],pair[1][0]))
            sublist=list()

