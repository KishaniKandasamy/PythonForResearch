#with multiple varibales
# y = (m1*x1 + m2*x2 +m3*x3) + b

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import math
%matplotlib inline

df=pd.read_csv("homeprice(MLR).csv")


#Remove null value ->Replace it with median #datapreprocessing
median_bedrooms=math.floor(df.Bedrooms.median()) #to make 3.5 to 3
#median_bedrooms

df.Bedrooms=df.Bedrooms.fillna(median_bedrooms)

reg=linear_model.LinearRegression()

#independent features and target feature
reg.fit(df[['Area','Bedrooms','Age']], df.Price)

#reg.coef_  #m1,m2,m3
#reg.intercept_

reg.predict([[3000,4,40]])
