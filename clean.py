#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#loading Data
df=pd.read_csv(r"E:\python\Zomato data project\Zomato data .csv",encoding='latin1')

#cleaning Data
def handleval(value):
    value=str(value).split('/')   #function to remove /5
    value=value[0]
    return float(value)

df['rate']=df['rate'].apply(handleval)
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.head())

#Now plotting charts
#Types of Restraunts(Bar-Charts)
# type_counts=df['listed_in(type)'].value_counts()
# plt.bar(type_counts.index,type_counts.values,color='coral',
#         label='Types of Restraunt(s) Bar-Chart')
# plt.title('Types of Restraunts')
# plt.xlabel('Restraunts type')
# plt.ylabel('Number of Restraunts')
# plt.legend()
# plt.show()

# #Online Orders yes or no(pie-chart)
# type_counts=df['online_order'].value_counts()
# plt.pie(type_counts.values,labels =type_counts.index,autopct='%1.1f%%')
# plt.title('Online Oders Data')
# plt.show()

# #Which type of Restraunts has Most votes(line-chart)
# grpdt=df.groupby('listed_in(type)')['votes'].sum()
# result=pd.DataFrame({'votes':grpdt})
# plt.plot(result,color='purple',marker='o')
# plt.grid(color='grey',linestyle=':')
# plt.xlabel('Types of Restraunts')
# plt.ylabel('Votes for restraunts')
# plt.show()

#Maximum ratings Recived(Histogram-chart)
plt.hist(df['rate'],bins=5)
plt.title('Majority Ratings recived')
plt.show()