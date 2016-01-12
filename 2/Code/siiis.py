import networkx as nx
import matplotlib.pyplot as plt
import random
import csv

def siiis (g,seeds,beta1,gamma1,beta2,gamma2,beta3,gamma3):
    tmax=1000
    #beta=0.3
    #gamma=0.5

    S=set()
    I1=set()
    I2=set()
    I3=set()
    R=set()
    epicurve1=list()
    epicurve2=list()
    epicurve3=list()
    recover=list()

    #Select "seeds" random nodes from graph.

    for i in range(0,seeds):
        node = random.choice(g.nodes()) #assuming no same nodes are picked in choice
        I1.add(node)
        node = random.choice(g.nodes()) #assuming no same nodes are picked in choice
        if node not in I1:
            I2.add(node)
        node = random.choice(g.nodes()) #assuming no same nodes are picked in choice
        if node not in I2 and node not in I1:
            I3.add(node)
        
    epicurve1.append(len(I1))
    epicurve2.append(len(I2))
    epicurve3.append(len(I3))
    
    #start time
    for t in range(1,tmax):
        print t
    #######recovery#############################

        if(t>1):
            recovery_num1=int(round(gamma1*len(I1)))
            for i in range(0,recovery_num1):
                node1=random.sample(I1,1)
                #R.add(node[0])
                I1.discard(node1[0])

            recovery_num2=int(round(gamma2*len(I2)))
            for i in range(0,recovery_num2):
                node2=random.sample(I2,1)
                #R.add(node[0])
                I2.discard(node2[0])

            recovery_num3=int(round(gamma3*len(I3)))
            for i in range(0,recovery_num3):
                node3=random.sample(I3,1)
                #R.add(node[0])
                I3.discard(node3[0])
            

    ################infection 1################################  

        # recover people
        

        

        #create susceptible set
        for node in set(I1):
            neighbours = g.neighbors(node)
            S=set()
            for neighbour in neighbours:
                if neighbour not in set(I2.union(I3)):
                    S.add(neighbour)
        
        #infect more people
        infected_num= int(round(beta1*len(S)))

        #spread infection
        for i in range(0,infected_num):
            node=random.sample(S,1)
            I1.add(node[0])
            S.discard(node[0])

        epicurve1.append(len(I1))
        #recover.append(len(R))


    ################infection 2################################  

        # recover people
        

        

        #create susceptible set
        for node in set(I2):
            neighbours = g.neighbors(node)
            S=set()
            for neighbour in neighbours:
                if neighbour not in set(I1.union(I3)):
                    S.add(neighbour)
        
        #infect more people
        infected_num= int(round(beta2*len(S)))

        #spread infection
        for i in range(0,infected_num):
            node=random.sample(S,1)
            I2.add(node[0])
            S.discard(node[0])

        epicurve2.append(len(I2))
        #recover.append(len(R))

        ################infection 3################################  

        # recover people
       

        

        #create susceptible set
        for node in set(I3):
            neighbours = g.neighbors(node)
            S=set()
            for neighbour in neighbours:
                if neighbour not in set(I1.union(I2)):
                    S.add(neighbour)
        
        #infect more people
        infected_num= int(round(beta3*len(S)))

        #spread infection
        for i in range(0,infected_num):
            node=random.sample(S,1)
            I3.add(node[0])
            S.discard(node[0])

        epicurve3.append(len(I3))

    return (epicurve1,epicurve2,epicurve3)



    
g=nx.Graph()
count=0

#g=nx.fast_gnp_random_graph(100,0.3)
with open("dataset.dat",'r')as myfile:
	for line in myfile:
		count=count+1
		if count>0:
			line=line.strip('\n')
			line=line.strip('\t')
			val=line.split(" ")
			if val[0]=='':
				new=1		

			if val[0]!='':
				if new==1:
					new=0
					node1=val[0]
				else:
					#print node1,val[0]
					g.add_edge(node1,val[0])
		else:
			break


r1,r2,r3=siiis(g,5,0.3,0.5,0.4,0.6,0.3,0.7)                      

filewrite=open("siiis_test.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in zip(r1,r2,r3):
	wr.writerow(item)



