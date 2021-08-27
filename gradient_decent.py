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
   
       
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost_MSE = (1/n) * sum([val**2  for val in (y- y_predicted)])
        md = -(2/n) * sum( x * (y - y_predicted)) # m derivative
        bd = -(2/n) * sum(y - y_predicted) # b derivative
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m = {} , b= {} ,cost = {} iteration = {} ".format(m_curr,b_curr,cost_MSE, i))

gradient_decent(x,y)
