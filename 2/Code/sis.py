import networkx as nx
import matplotlib.pyplot as plt
import random
import csv

def sis(g,seeds,beta,gamma):
	tmax=1000

	S=set()
	I=set()
	#R=set()
	epicurve=list()
	recover=list()
	
	for i in range(0,seeds):
		node = random.choice(g.nodes())
		I.add(node)
	epicurve.append(len(I))
	
	for t in range(1,tmax):
		print t
		if (t>1):
			recovery_num=int(round(gamma*len(I)))
			for i in range(0,recovery_num):
				node=random.sample(I,1)
				#R.add(node[0])
				I.discard(node[0])
		
		for node in set(I):
			neighbours=g.neighbors(node)
			S=set()
			for neighbour in neighbours:
				if neighbour not in set(I):
					S.add(neighbour)
		infected_num=int(round(beta*len(S)))
		
		for i in range(0,infected_num):
			node=random.sample(S,1)
			I.add(node[0])
			S.discard(node[0])

		epicurve.append(len(I))
	
	
	return epicurve

#G=nx.fast_gnp_random_graph(1000,0.1)
g=nx.Graph()
count=0

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
#print g.edges()

#result=list()
re5sum=[0]*1000
for i in range(0,10):
        result5=sis(g,5,0.3,0.5)
        re5sum[:]=map(sum,zip(result5,re5sum))
        print i

re5sum[:]=[float(x)/10 for x in re5sum]

print re5sum


filewrite=open("sis5.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in re5sum:
	wr.writerow([item])


		
re50sum=[0]*1000
for i in range(0,10):
        result50=sis(g,50,0.3,0.5)
        re50sum[:]=map(sum,zip(result50,re50sum))
        print i

re50sum[:]=[float(x)/10 for x in re50sum]

print re50sum


filewrite=open("sis50.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in re50sum:
	wr.writerow([item])



re100sum=[0]*1000
for i in range(0,10):
        result100=sis(g,100,0.3,0.5)
        re100sum[:]=map(sum,zip(result100,re100sum))
        print i

re100sum[:]=[float(x)/10 for x in re100sum]

print re100sum




filewrite=open("sis100.csv",'wb')
wr=csv.writer(filewrite,dialect='excel')
for item in re100sum:
	wr.writerow([item])







