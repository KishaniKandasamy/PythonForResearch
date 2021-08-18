from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
%matplotlib inline

df = pd.read_csv("income.csv")
#df.head()

#Scale down the values for better visualization

scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)']= scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age']= scaler.transform(df[['Age']])



#find optimal K using elbow method

krange = range(1,10)

sse = []  #sum of squared errors

for k in krange:
    km=KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)
 
  #plt.xlabel='k'
#plt.ylabel='sse'
#plt.plot(krange,sse);


#Clustering with optimal val of k = 3

km=KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
#y_predicted

df['cluster']=y_predicted
#df
df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]

plt.scatter(df1['Age'],df1['Income($)'],color ='green',label="cluster0")
plt.scatter(df2['Age'],df2['Income($)'],color ='red',label="cluster1")
plt.scatter(df3['Age'],df3['Income($)'],color ='yellow',label="cluster2")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color = "blue",marker="*" ,label="centroid")

plt.xlabel='Age'
plt.ylabel='Income($)'
plt.legend(loc= "upper left") 

       
