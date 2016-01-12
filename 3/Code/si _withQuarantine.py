import networkx as nx
import matplotlib.pyplot as plt
import random
import operator
import csv

def si(g,gfear,seeds,beta,fseeds,fbeta):
        tmax=100

        S={}
        I={}
        Sfear={}
        Ifear={}
        #R=set()
        epicurve=list()
        epicurvefear=list()
        recover=list()
        
        for i in range(0,seeds):
                node = random.choice(g.nodes())
                I[node]=0
        epicurve.append(len(I))

        #select fear nodes on some heuristic
        nodeDict=nx.eigenvector_centrality(gfear,tol=1e-03);
        sorted_Node = sorted(nodeDict.items(), key=operator.itemgetter(1))
        rsorted_Node=sorted_Node[::-1];
        print "seed nodes"
        
        for i in range(0,fseeds):
##                node = random.choice(gfear.nodes())
##                Ifear[node]=0
                Ifear[rsorted_Node[i][0]]=0
##                print rsorted_Node[i]
                
        epicurvefear.append(len(Ifear))
        
        
        for t in range(1,tmax):
                
                
                print t
                Sfear={}
                S={}
                if(t>25):
                        if(t==26):
                                epiInitial=list(epicurve);
                                
                        #spread fear
                        for nodef in Ifear:
                                neighboursf=gfear.neighbors(nodef)
                                
                                for neighbourf in neighboursf:
                                        if neighbourf not in Ifear:
                                                Sfear[neighbourf]=0
                        infected_numf=int(round(fbeta*len(Sfear)))

                        for i in range(0,infected_numf):
                                nodef=random.sample(Sfear,1)
                                Ifear[nodef[0]]=0
                                #remove node from contact network
                                g.remove_node(nodef[0]);
                                if nodef[0] in set(I):
                                        del I[nodef[0]];
                                
                                del Sfear[nodef[0]]

                        epicurvefear.append(len(Ifear))
                        print "fear is",len(Ifear)


                        #spread disease
                        
                        for node in I:
                                neighbours=g.neighbors(node)
                              
                                for neighbour in neighbours:
                                        if neighbour not in I:
                                                S[neighbour]=0
                        infected_num=int(round(beta*len(S)))
                        
                        for i in range(0,infected_num):
                                node=random.sample(S,1)
                                I[node[0]]=0
                                del S[node[0]]

                        epicurve.append(len(I))
                        print "disease spread is",len(I)

                        
                        
                else:
                        
                        
                        for node in I:
                                neighbours=g.neighbors(node)
                              
                                for neighbour in neighbours:
                                        if neighbour not in I:
                                                S[neighbour]=0
                        infected_num=int(round(beta*len(S)))
                        
                        for i in range(0,infected_num):
                                node=random.sample(S,1)
                                I[node[0]]=0
                                del S[node[0]]

                        epicurve.append(len(I))
                        print "disease spread is",len(I)

        #write fear epicurve
        filewrite=open("siepifear.csv",'wb')
        wr=csv.writer(filewrite,dialect='excel')
        for item in epicurvefear:
                wr.writerow([item])


##         #write fear first26 epicurve
##        filewrite=open("siepi25.csv",'wb')
##        wr=csv.writer(filewrite,dialect='excel')
##        for item in epiInitial:
##                wr.writerow([item])
        
        
        filewrite=open("sitotal.csv",'wb')
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

result10=si(g,gfear,10,0.3,10,0.6)

##filewrite=open("sitotal.csv",'wb')
##wr=csv.writer(filewrite,dialect='excel')
##for item in result10:
##      wr.writerow([item])






