import networkx as nx
import matplotlib.pyplot as plt
import random
import csv
import operator

def sir(g,seeds,beta,gamma):
        tmax=100

        S={}
        I={}
        R={}
        epicurve=list()
        recover=list()
        
        for i in range(0,seeds):
                node = random.choice(g.nodes())
                I[node]=0
        epicurve.append(len(I))
        
        for t in range(1,tmax):
                #print t
                S={}
                if (t>1):
                        recovery_num=int(round(gamma*len(I)))
                        for i in range(0,recovery_num):
                                node=random.sample(I,1)
                                R[node[0]]=0
                                del I[node[0]]
                
                for node in I:
                        neighbours=g.neighbors(node)
                        #S=set()
                        for neighbour in neighbours:
                                if neighbour not in R and neighbour not in I:
                                        S[neighbour]=0
                infected_num=int(round(beta*len(S)))
                
                for i in range(0,infected_num):
                        node=random.sample(S,1)
                        I[node[0]]=0
                        del S[node[0]]


                epicurve.append(len(I))
                print(len(I))
        
        
        return epicurve

	

#G=nx.fast_gnp_random_graph(1000,0.1)
#g=nx.Graph()
mainG=nx.read_edgelist("gowalla_edges_contact.txt")
count=0

##with open("dataset.dat",'r')as myfile:
##	for line in myfile:
##		count=count+1
##		if count>0:
##			line=line.strip('\n')
##			line=line.strip('\t')
##			val=line.split(" ")
##			if val[0]=='':
##				new=1		
##
##			if val[0]!='':
##				if new==1:
##					new=0
##					node1=val[0]
##				else:
##					#print node1,val[0]
##					g.add_edge(node1,val[0])
##		else:
##			break
##print g.edges()

#result=list()
############for 5 nodes


##re5sum=[0]*1000
##for i in range(0,100):
##        result5=sir(g,5,0.3,0.5)
##        re5sum[:]=map(sum,zip(result5,re5sum))
##        print i
##
##re5sum[:]=[float(x)/100 for x in re5sum]
##
##print re5sum
##
##
##filewrite=open("sir5.csv",'wb')
##wr=csv.writer(filewrite,dialect='excel')
##for item in re5sum:
##	wr.writerow([item])


########for 50 nodes

        #remove random 50 nodes;
g = mainG.copy();
nodeDict=nx.eigenvector_centrality(g,tol=1e-03);
sorted_Node = sorted(nodeDict.items(), key=operator.itemgetter(1))
rsorted_Node=sorted_Node[::-1];
for j in range(0,100):
        #nodeRem = random.choice(g.nodes())
        if g.has_node(rsorted_Node[j]):
                g.remove_node(rsorted_Node[j]);


result50=sir(g,50,0.3,0.5)
del g;


filewrite=open("sirRem50.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in result50:
	wr.writerow([item])


##############for 100 nodes
	
##re100sum=[0]*1000
##for i in range(0,100):
##        result100=sir(g,100,0.3,0.5)
##        re100sum[:]=map(sum,zip(result100,re100sum))
##        print i
##
##re100sum[:]=[float(x)/100 for x in re100sum]
##
##print re100sum
##
##
##
##
##filewrite=open("sir100.csv",'wb')
##wr=csv.writer(filewrite,dialect='excel')
##for item in re100sum:
##	wr.writerow([item])






