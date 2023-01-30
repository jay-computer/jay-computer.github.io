#run make file, run ./spheres input, change input as necessary

import random
import math
from matplotlib import pyplot as plt
import numpy as np
import csv
from matplotlib.patches import Circle

RJ_input = np.empty(1)

with open('write.dat') as f:
    reader = csv.reader(f, delimiter="\n")
    
    for line in reader:
        RJ_input = np.append(RJ_input, line)
        
circ_radii = float(RJ_input[4]) / 2
print("Diamter: {}".format(circ_radii*2))
print(RJ_input[7])
RJ_input = RJ_input[7:]        
#print(RJ_input)
#print(np.char.split(RJ_input))



RJ_input = np.char.split(RJ_input)

#print([float(row[0]) for row in RJ_input])
RJ_x = [float(row[0]) for row in RJ_input]

#print([float(row[1]) for row in RJ_input])
RJ_y = [float(row[1]) for row in RJ_input]



#for i in range(0, len(RJ_input)):
#plt.plot(RJ_x, RJ_y, marker = 'o', markersize = circ_radii)    

fig,ax = plt.subplots(1)
ax.set_aspect('equal')

lowerbound = -0.1
upperbound = 1.1

scale = False
if scale == True:
    circ_radii = circ_radii * 10
    lowerbound = lowerbound * np.sqrt(10)
    upperbound = upperbound * np.sqrt(10)
    

ax.set(xlim=(lowerbound, upperbound), ylim=(lowerbound, upperbound))
for i in range(0, len(RJ_input)):
    circ = Circle((RJ_x[i], RJ_y[i]), circ_radii, fill=False)
    ax.add_patch(circ)
    

big_circ = Circle((0.5, 0.5), 0.5, fill=False, color='r')
ax.add_patch(big_circ)