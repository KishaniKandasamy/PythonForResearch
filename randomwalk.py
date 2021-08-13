import random
import matplotlib.pyplot as plt
import numpy as np

#from the origin
X_O = np.array([[0],[0]])

delta_X=np.random.normal(0,1,(2, 100))
plt.plot(delta_X[0],delta_X[1],"go")

#find cumulative sum of displacements
X=np.cumsum(delta_X, axis=1)

#concatenate numpy arrays 
X=np.concatenate((X_O,X), axis=1)

#plot the random walks
plt.plot(X[0],X[1] ,"ro-");
