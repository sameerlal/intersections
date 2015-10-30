import random
from sys import argv

script, out = argv
iterations = raw_input("Enter interations: " + "\n" + ">>")
outfile = open(out, 'w')
outfile.write("seed -- A -- B -- C -- D" + "\n")
for i in range(1, int(iterations)+1):
	outfile.write(str(i) + "," + str(random.randint(0,3)) + "," + str(random.randint(0,3)) + "," + str(random.randint(0,3)) + "\n")
	# Uncomment next line for console output
	# print (str(i) + "," + str(random.randint(0,3)) + "," + str(random.randint(0,3)) + "," + str(random.randint(0,3)))
outfile.close()



