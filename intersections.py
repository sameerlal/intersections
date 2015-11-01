from numpy import genfromtxt


stuff = open('sample1.txt','r')
Adata =[]
Bdata =[]
Cdata =[]
Ddata = []

my_data = genfromtxt('sample1.txt', delimiter = ',')

print my_data


# num_line = sum(1 for line in open('sample1.txt')) 
# for i in range(1,num_line):
# 	hello = 3+i



	