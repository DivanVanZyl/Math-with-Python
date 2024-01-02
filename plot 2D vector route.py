from ast import Str
from turtle import color
import matplotlib.pyplot as plt;
import random

# vectors to plot
SIZE = 10
VECTOR_X_MAX = 10
VECTOR_X_MIN = 1
VECTOR_Y_MAX = 10
VECTOR_Y_MIN = 1

vectors = []
bigVector = [0,0]

# Loop and create x amount of new vectors, where the next one's origin, is the previous one's distination
for i in range(0,SIZE):
    temp = [int(random.uniform(VECTOR_X_MIN, VECTOR_X_MAX)),int(random.uniform(VECTOR_Y_MIN, VECTOR_Y_MAX))]
    vectors.append(temp) 

print(vectors)

# Create a new vector, which is the sum of all the other vectors
for i in range(0,SIZE):
       for index in range(0,2):
           bigVector[index] += vectors[i][index]  
    

# Plot smaller vectors
prevEnd = [0,0] # Previous vector's end, is the current vector's origin
for i in range(0,SIZE):
    print(str(i) + " : " + "origin " + " x = " + str(prevEnd[0]) + " y = " + str(prevEnd[1]) + " values " + " x = " + str(vectors[i][0]) + " y = " + str(vectors[i][1]))
    plt.quiver(prevEnd[0],prevEnd[1],vectors[i][0],vectors[i][1], angles="xy", scale_units="xy", scale=1, color="red")
    prevEnd[0] += vectors[i][0]
    prevEnd[1] += vectors[i][1]

# Plot big boi vector
plt.quiver(0,0,bigVector[0],bigVector[1], angles="xy", scale_units="xy", scale=1, color="blue")     

plt.xlim([0,75])  #Put limits on x axis
plt.ylim([0,75])  #Put limits on y axis

plt.xlabel("X")
plt.xlabel("Y")

plt.grid()

# Big boi vector should start and end at the same places as the collection of vectors
plt.show()