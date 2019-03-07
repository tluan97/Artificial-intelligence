# Visualization

import numpy as np
import matplotlib.pyplot as plt

## Create a array x and y
#x = list(range(1,11))
#y = [i**2 for i in x]
#
## Show dot
#plt.scatter(x, y, s=100, edgecolor='blue', c='green')
#
## Show line
#plt.plot(x, y, color='red')
#
## Size of plt
#plt.tick_params(axis = 'both', which = 'major', labelsize=15)
#
## Limit x and y
##plt.axis([0,10,0,100])
#
## Title, label
#plt.title('Square', size=20)
#plt.xlabel('i', size=20)
#plt.ylabel('i^2', size=20)
#
## Show
#plt.show()

#import secrets as sc
#from random import randint
#
## Random a 2D table
#a = []
#b = []
#t = list(range(0,1001))
#for i in range(0,1001):
#    a.append(randint(0,1001))
#    b.append(sc.choice(t))
#
#plt.scatter(a, b, c=t, cmap=plt.cm.Reds, s=10)
#
## Remove the axes
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)
#plt.show()


#import pygal
#from random import randint
#
## Analyze the results.
#frequencies = []
#for i in range(1,7):
#    frequency = randint(1,7)
#    frequencies.append(frequency)
#
## Visualize the results.
#hist = pygal.Bar()
#hist.title = "Results of rolling one D6 1000 times."
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
#hist.x_title = "Result"
#hist.y_title = "Frequency of Result"
#hist.add('D6', frequencies)
#hist.render_to_file('die_visual.svg')

#from matplotlib import pyplot
#from mpl_toolkits.mplot3d import Axes3D
#import random
#
#fig = pyplot.figure()
#ax = Axes3D(fig)
#
#x_vals = list(range(0, 1001))
#y_vals = list(range(0, 1001))
#z_vals = list(range(0, 1001))
#
#random.shuffle(x_vals)
#random.shuffle(y_vals)
#random.shuffle(z_vals)
#
#ax.scatter(x_vals, y_vals, z_vals)
#pyplot.show()

