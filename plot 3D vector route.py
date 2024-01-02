from ast import Str
from turtle import color
import matplotlib.pyplot as plt;
import random

fig = plt.figure()

ax = fig.add_subplot(111,projection = "3d")

# vectors to plot
SIZE = 10
VECTOR_X_MAX = 10
VECTOR_X_MIN = 1
VECTOR_Y_MAX = 10
VECTOR_Y_MIN = 1
VECTOR_Z_MAX = 10
VECTOR_Z_MIN = 1

vectors = []
bigVector = [0,0,0]

# Loop and create x amount of new vectors, where the next one's origin, is the previous one's distination
for i in range(0,SIZE):
    temp = [int(random.uniform(VECTOR_X_MIN, VECTOR_X_MAX)),int(random.uniform(VECTOR_Y_MIN, VECTOR_Y_MAX)),int(random.uniform(VECTOR_Y_MIN, VECTOR_Y_MAX))]
    vectors.append(temp) 

print(vectors)

# Create a new vector, which is the sum of all the other vectors
for i in range(0,SIZE):
       for index in range(0,3):
           bigVector[index] += vectors[i][index]  
    

# Plot smaller vectors
prevEnd = [0,0,0] # Previous vector's terminal point, is the current vector's origin
for i in range(0,SIZE):
    print(str(i) + " : " + "origin " + " x = " + str(prevEnd[0]) + " y = " + str(prevEnd[1]) + " z = " + str(prevEnd[2]) + " values " + " x = " + str(vectors[i][0]) + " y = " + str(vectors[i][1]) + " z = " + str(vectors[i][2]))
    ax.quiver(prevEnd[0],prevEnd[1],prevEnd[2],vectors[i][0],vectors[i][1],vectors[i][2], color="red", arrow_length_ratio=0.1)
    prevEnd[0] += vectors[i][0]
    prevEnd[1] += vectors[i][1]
    prevEnd[2] += vectors[i][2]

# Plot big boi vector
ax.quiver(0,0,0,bigVector[0],bigVector[1],bigVector[2], color="blue", arrow_length_ratio=0.02)     

ax.set_xlim([0,75])
ax.set_ylim([0,75])
ax.set_zlim([0,75])

#set labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#Title
plt.title("3D Vector Plot")

ax.grid()

# Big boi vector should start and end at the same places as the collection of vectors
plt.show()