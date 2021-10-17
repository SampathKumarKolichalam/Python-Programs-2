#Importing Librarires:-
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from seaborn.distributions import kdeplot

#Reading Dataset:-
ds=sns.load_dataset("tips")
#print(ds.head())
#print(ds.tail())
#print(ds.describe())

#Displot:-Univarite(Single Variable) (kde+hist both)
#sns.displot(ds["total_bill"],kde=True)
#plt.show()

#Histrogram:-(hist only)
#sns.displot(ds["total_bill"],kde=False)
#plt.show()

#kernel Density Estimates:-(kde only)
#sns.displot(ds["total_bill"],hist=False)
#plt.show()

#JointPlot():-Bivarite(Two Variables)(dots+graph both)
#sns.jointplot(x="total_bill",y="tip",data=ds)
#plt.show()

#ScatterPlot():-(dots only)
#sns.scatterplot(x="total_bill",y="tip",data=ds)
#plt.show()

#PairPlot():-
#sns.set_style("ticks")
#sns.pairplot(ds)
#plt.show()

#StripPlot():-
#sns.stripplot(x="day",y="total_bill",data=ds,jitter=True)
#plt.show()

#SwarmPlot():-
#sns.swarmplot(x="day",y="total_bill",data=ds)
#plt.show()

#BoxPlot():-
#sns.boxplot(x=ds["total_bill"])
#plt.show()

#ViolinPlot():-
#sns.violinplot(x=ds["total_bill"])
#plt.show()

#BarPlot():-
#sns.barplot(x="day",y="total_bill",data=ds)
#plt.show()

#PointPlot():-
#sns.pointplot(x="time",y="total_bill",data=ds)
#plt.show()

#RegPlot():-
#sns.regplot(x="total_bill",y="tip",data=ds)
#plt.show()

#LM Plot():-
#sns.regplot(x="total_bill",y="tip",data=ds)
#plt.show()

#HeatMap():-
#uniform_data=np.random.rand(10,12)
#sns.heatmap(uniform_data)
#plt.show()

#ClusterMap():-
#df=ds[["total_bill","tip","size"]]
#sns.clustermap(df)
#plt.show()

