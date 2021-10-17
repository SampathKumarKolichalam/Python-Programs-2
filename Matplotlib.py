import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import median
#Line Plot:-
x=np.arange(1,6)
y=2*x
z=3*x
plt.plot(x,y,"o")
plt.plot(x,marker="o",ms=10,mec="b",mfc="y")
plt.plot(x,y,colocr="r",linestyle="dotted",linewidth=5,markersize=10)

plt.plot(x,y,label="X")
plt.plot(x,z,label="Z")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.plot(x,y,alpha=0.5)
plt.subplot(1,2,2)
plt.legend("best")
plt.legend(fontsize="small")
plt.grid()
plt.show()
#Bar plot and Horizontal bar plot:-
companies=["Infosys","Amazon","IBM","TCS"]
revenue=[40,50,30,35]
profit=[25,20,25,30]
plt.bar(companies,revenue,label="Revenue")#:-Vertical bar plot.
plt.bar(companies,profit,label="Profit")#:-Vertical bar plot.
#plt.barh(companies,revenue,label="Revenue"):-Horizontal bar plot.
#plt.barh(companies,profit,label="Profit"):-Horizotal bar plot.
plt.xlabel("Companies")
plt.ylabel("Revenue")
plt.title("Bar Plot of Tech companies revenue")
plt.grid(True)
plt.legend()
plt.show()
#Histogram:-
data=[1,2,2,3,3,3,4,4,4,4]
plt.hist(data,bins=3,rwidth=0.9,color="g")
plt.xlabel("Data")
plt.ylabel("Data Occurance")
plt.title("Histogram plot")
plt.show()
#Box plot:-
l1=[1,2,3,4]
l2=[4,5,7,2]
l3=[3,7,2,5]
data=list([l1,l2,l3])
plt.boxplot(data)
plt.show()
#Scatter Plot:-
x=[1,3,6,4]
y=[2,4,5,6]
x1=[2,4,5,6]
y1=[1,3,6,4]
plt.scatter(x,y,marker="*",s=50)
plt.scatter(x1,y1,marker="+",s=50)
plt.show()
#Pie Chart:-
exp_types=["Home Rent","Food","Bills","Travelling","Other uses","Savings"]
exp_values=[3000,4000,1000,2500,1500,20000]
plt.pie(exp_values,labels=exp_types,autopct="%d%%",explode=[0,0.2,0.1,0,0,0])
plt.title("Monthly Expenditure")
plt.show()
#Violin Plot:-
l1=[1,2,3,4]
l2=[4,5,7,2]
l3=[3,7,2,5]
data=list([l1,l2,l3])
plt.violinplot(data,showmedians=True)
plt.show()
#DoughNut Chart:-
fruit=["Orange","Guava","Apple","Mango"]
Price=[70,80,120,40]
plt.pie(Price,labels=fruit,radius=1,colors=["orange","green","red","yellow"])
plt.pie([2],colors=["pink"],radius=0.5)
plt.show()
