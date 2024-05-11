import pandas as pd 

printx = lambda x : print(x,end='\n\n\n')

daset = pd.read_csv("pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/auto-mpg.csv");
# # #printx(daset)
# # #printx(daset.info())
# #printx(daset.head()) 
# #  first 5 
# #printx(daset.head(7))
# # first 7 
# #printx(daset.tail()) # last 5 
# #printx(daset.head(10)) # last 10 

# # row , column
# #printx(daset.shape)

# #printx(daset.loc[[394,396]])
# #printx(daset.loc[34:396:10]) 

# #printx('\n'*2)
# #printx(daset.loc[397][0])
# # #printx('\n'*2)
# # #printx(daset.loc[397][-1])
# #printx('\n'*2)
# # #printx(daset[0].iloc[[397]])

# #printx([*daset.columns])

# #printx('\n'*2)
# #printx(daset.describe())

# #printx(daset.describe(percentiles=[0.3,0.45,0.1])[['mpg','weight']])


# # how to take out percentiles of first 50 
# #printx(daset[0:2].describe(include='all') )


import numpy as np

printx(daset.describe(include=np.object_))
printx('\n\n\n')
printx(daset.describe(exclude=np.object_))
printx('\n\n\n')
printx(daset.describe(exclude=np.number))
printx('\n\n\n')
# printx(daset.describe(exclude="all"))
printx(daset.describe(include="all"))
printx('\n\n\n')
printx(daset.describe(exclude=None))
printx('\n\n\n')

df = pd.read_csv("pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/auto-mpg.csv")

# pd = False

import matplotlib.pyplot as plt
printx(df.corr(numeric_only=True))
# pd.plotting.scatter_matrix(df,figsize=[15,15],diagonal='kde')
# plt.show()

# printx(pd.__version__)



from pandas.plotting import parallel_coordinates
 
# pll = parallel_coordinates(df,'mpg',cols=['acceleration','mpg','origin'],color=['aqua','red','blue','orange',])
# plt.show()

printx('\n')
printx('\n')
printx(pd.crosstab(df["cylinders"],df['model year'],rownames=['cylinders'],colnames=['model year']))


import numpy as np 

sales_data = pd.DataFrame({  'name' : ['A','B','C','D','E','F','G',np.nan,'H','I','J'],
                          'region' : [np.nan,"North",'East',np.nan,'West','West','South',np.nan,'West','East','South'],
                          'sales': [50000,5299,np.nan,np.nan,42000,72000,49000,np.nan,67000,65000,67000],
                          'expenses': [42000,43000,np.nan,np.nan,38000,39000,42000,np.nan,39000,50000,45000]
                          })

printx(sales_data)
printx(sales_data.isna().sum())
printx(sales_data.dropna(axis=1))
printx(sales_data.dropna(axis=0))


# only remove colmn which have only 2 data and others are  nan
printx(sales_data.dropna( axis=1,thresh=9))


printx( (sales_data.dropna(subset=['sales','expenses'])))
printx(sales_data)

# printx(sales_data.dropna(inplace=True))
printx(sales_data)

x = sales_data.fillna(0)
printx(x)
printx(sales_data)

x = sales_data.copy()
x.fillna(0,inplace=True)
printx(x)


sales_data_copy = sales_data.copy()
sales_data_copy['sales'] =sales_data_copy['sales'].fillna(sales_data_copy['sales'].mean())
printx(sales_data_copy)

data = {
    'A' : ['TeamA','TeamB','TeamB','TeamC','TeamA'],
    'B' : [50,40,40,30,50],
    "C" : [True,False,False,False,True]
}


df = pd.DataFrame(data)
printx(df)
dups = df.duplicated()
printx(dups)



dups = df.drop_duplicates()
printx(dups)

printx(dups.reset_index())




# daset for auto-mpg

# we have a drop methode that remove given index raw or column 
#  if axis is 1 then we have to provide column name 


# if inmplese is True then it returns none other wise dataframe 

printx(daset)

dasetcopy = daset.copy().drop('mpg',axis=1)
printx(dasetcopy)

printx(daset['horsepower']=='?')
printx(daset[daset['horsepower']=='?'])
