import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
%matplotlib inline

df= pd.read_csv('homeprice.csv')
plt.xlabel('area(sqr ft)')
plt.ylabel('price($)')
plt.scatter(df.Area, df.Price, color='red',marker='*')

reg=linear_model.LinearRegression()
reg.fit(df[['Area']],df.Price) #train the model

#reg.predict([[3300]])
reg.coef_

reg.intercept_

dftest=pd.read_csv('testdata.csv')
predicted=reg.predict(dftest)
dftest['Price-predicted']=predicted
dftest.to_csv('prediction.csv',index=False)

plt.xlabel('area(sqr ft)', fontsize=20)
plt.ylabel('price($)' , fontsize=20)
plt.scatter(df.Area, df.Price, color='red',marker='*')
plt.plot(df.Area,reg.predict(df[['Area']]),color='green')
