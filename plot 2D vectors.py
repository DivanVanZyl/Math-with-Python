from turtle import color
import matplotlib.pyplot as plt;

v1 = [2,0]
v2 = [0,5]
v3 = [2,5]   #vector to plot


plt.quiver(0,0,v1[0],v1[1], angles="xy", scale_units="xy", scale=1, color="red")
plt.quiver(v1[0],v1[1],v2[0],v2[1], angles="xy", scale_units="xy", scale=1, color="blue")
plt.quiver(0,0,v3[0],v3[1], angles="xy", scale_units="xy", scale=1, color="green")

plt.xlim([0,10])  #Put limits on x axis
plt.ylim([0,10])  #Put limits on y axis

plt.xlabel("X")
plt.xlabel("Y")

plt.grid()

plt.show()