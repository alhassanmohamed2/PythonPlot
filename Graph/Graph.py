from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt
from matplotlib import pyplot , pylab 
import numpy as np
from math import e



fig = pyplot.figure() 
ax = fig.add_subplot(111, projection='3d')

n=np.arange(-3,3,.125)
[X,Y] = np.meshgrid(n,n)

a = ((3*(1-X)**2) * np.power(e,(-X**2 - (Y+1)**2)))
b = (10*(X/5 - X**3 - Y**5) * np.power(e,(-X**2 - Y**2)))
c= (1/3 * np.power(e,(-(X+1)**2 - Y**2)))
Z = a - b - c


ax.plot_wireframe(X,Y,Z, rstride=4, cstride=5)

ax.plot_surface(X, Y, Z,cmap='jet', edgecolor='none')
ax.view_init(elev=23, azim=-159)
plt.title("Graph Visualization")
pylab.gcf().canvas.set_window_title("Graph Visualization")
plt.grid(False)
plt.axis('off')
plt.show()
