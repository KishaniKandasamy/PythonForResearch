import numpy as np

# y=mx+c -->  y=2x+3 @min MSE get the optimal m and b
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

def gradient_decent(x,y):
   #initialise with 0
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x) #no of data points 
    learning_rate = 0.01
