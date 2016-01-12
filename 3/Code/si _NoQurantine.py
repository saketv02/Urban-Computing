import networkx as nx
import matplotlib.pyplot as plt
import random
import csv

def si(g,gfear,seeds,beta,fseeds,fbeta):
        tmax=100

        S={}
        I={}
        Sfear=set()
        Ifear=set()
        #R=set()
        epicurve=list()
        epicurvefear=list()
        recover=list()
        
        for i in range(0,seeds):
                node = random.choice(g.nodes())
                I[node]=0;
        epicurve.append(len(I))

        #select fear nodes on some heuristic
        for i in range(0,fseeds):
                node = random.choice(gfear.nodes())
                Ifear.add(node)
        epicurvefear.append(len(Ifear))
        
        
        for t in range(1,tmax):
                
                
                        print t     
                
                        S={}
                        for node in I:
                                neighbours=g.neighbors(node)
                                #S=set()
                                #print "Node is",node
                                for neighbour in neighbours:
                                       # print neighbour
                                        if neighbour not in I:
                                                #print "infected",neighbour
                                                S[neighbour]=0
                                                
                        infected_num=int(round(beta*len(S)))

                       
                        print "infected num is ",infected_num,len(S)
                                
                        for i in range(0,infected_num):
                                node=random.sample(S,1)
                                I[node[0]]=0
                                del S[node[0]]

                        epicurve.append(len(I))

        #write fear epicurve
       

         
        
        
        filewrite=open("sitotal_noq.csv",'wb')
        wr=csv.writer(filewrite,dialect='excel')
        for item in epicurve:
                wr.writerow([item])


#G=nx.fast_gnp_random_graph(1000,0.1)


g=nx.read_edgelist("gowalla_edges_contact.txt")
gfear=nx.read_edgelist("gowalla_edges_comm.txt")
count=0

##re10sum=[0]*25
##for i in range(0,10):
##        result10=si(g,10,0.3)
##        re10sum[:]=map(sum,zip(result10,re10sum))
##        print i
##
##re10sum[:]=[float(x)/10 for x in re10sum]
##
##print re10sum

si(g,gfear,10,0.3,10,0.1)

##filewrite=open("sitotal.csv",'wb')
##wr=csv.writer(filewrite,dialect='excel')
##for item in result10:
##      wr.writerow([item])






