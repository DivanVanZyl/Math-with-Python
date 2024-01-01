import matplotlib.pyplot as plt
import numpy as np

print("hello")

fig = plt.figure()

ax = fig.add_subplot(111,projection = "3d")


v1 = [1,2,3]
v2 = [-2,1,4]
v3 = [0,0,0]

for i in range(3):
    v3[i] = v1[i]+v2[i]

#actual plot here
#params: origin x, origin y, origin z, vector x, vector y, vector z, color, arrow astetics
ax.quiver(0,0,0,v1[0],v1[1],v1[2], color="r", arrow_length_ratio=0.1)
ax.quiver(0,0,0,v2[0],v2[1],v2[2], color="b", arrow_length_ratio=0.1)
ax.quiver(0,0,0,v3[0],v3[1],v3[2], color="g", arrow_length_ratio=0.1)

#Limits here
ax.set_xlim([-6,7])
ax.set_ylim([-6,7])
ax.set_zlim([-6,7])

#set labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#Title
plt.title("3D Vector Plot")

plt.show()
fig.savefig(r"C:\Users\Divan\Downloads\plot.png", dpi=1024)