import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


task1=pd.read_excel('data_tasks.xlsx',sheet_name='task1')
time = task1.values[:,0]
temp = task1.values[:,1]
std1 = task1.values[:,2]



plt.figure(1)
plt.title("Task 1",fontsize = 24)
plt.xlabel("Time(minute)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.errorbar(time,temp,yerr=std1,fmt="rs-",linewidth=3,elinewidth=.5,ecolor='k',capsize=5,capthick=1)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart1.png',dpi=600)


plt.figure(2)
plt.title("Task 1 Bar",fontsize = 24)
plt.xlabel("Time(minute)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.bar(time,temp,yerr = std1,align='center',ecolor='red',capsize=10,color="blue",edgecolor = 'white',)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart2.png',dpi=600)


task2=pd.read_excel('data_tasks.xlsx',sheet_name='task2')

tempLV = []
tempDO = []
tempDV = []
for i in task2.values[1:,1]:
    tempLV.append(i)
for i in task2.values[1:,3]:
    tempDO.append(i)
for i in task2.values[1:,5]:
    tempDV.append(i)
stdLV = []
stdDO = []
stdDV = []
for i in task2.values[1:,2]:
    stdLV.append(i)
for i in task2.values[1:,4]:
    stdDO.append(i)
for i in task2.values[1:,6]:
    stdDV.append(i)
time = []
for i in task2.values[1:,0]:
    time.append(i)
    
plt.figure(3)
plt.title(task2.columns[1],fontsize=24)
plt.xlabel("Time (Hour)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.errorbar(time,tempLV,yerr=stdLV,fmt="rs-",linewidth=3,elinewidth=.5,ecolor='k',capsize=5,capthick=1)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart3.png',dpi=600)


plt.figure(4)
plt.title(task2.columns[3],fontsize=24)
plt.xlabel("Time (Hour)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.errorbar(time,tempDO,yerr=stdDO,fmt="rs-",linewidth=3,elinewidth=.5,ecolor='k',capsize=5,capthick=1)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart4.png',dpi=600)


plt.figure(5)
plt.title(task2.columns[5],fontsize=24)
plt.xlabel("Time (Hour)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.errorbar(time,tempDV,yerr=stdDV,fmt="rs-",linewidth=3,elinewidth=.5,ecolor='k',capsize=5,capthick=1)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart5.png',dpi=600)


plt.figure(6)
plt.title(task2.columns[1],fontsize = 24)
plt.xlabel("Time(minute)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.bar(time,tempLV,yerr = stdLV,align='center',ecolor='red',capsize=10,color="blue",edgecolor = 'white',)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart6.png',dpi=600)


plt.figure(7)
plt.title(task2.columns[3],fontsize = 24)
plt.xlabel("Time(minute)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.bar(time,tempDO,yerr = stdDO,align='center',ecolor='red',capsize=10,color="blue",edgecolor = 'white',)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart7.png',dpi=600)

plt.figure(8)
plt.title(task2.columns[5],fontsize = 24)
plt.xlabel("Time(minute)",fontsize=14)
plt.ylabel("Tempurature(C)",fontsize=14)
plt.bar(time,tempDV,yerr = stdDV,align='center',ecolor='red',capsize=10,color="blue",edgecolor = 'white',)
plt.legend(["Standard Deviation"],loc='upper left')
plt.savefig('chart8.png',dpi=600)


