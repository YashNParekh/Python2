import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/yash/Desktop/Yash /Python2/pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/auto-mpg.csv")

# plt.boxplot(df['acceleration'],widths=0.75,notch=True)
# plt.show()
# print(df.describe())

values = [1,5,8,9,2,0,3,10,4,7]
# plt.plot(range(1,11),values)
# plt.show()


def find_outliers(ds,col) :
    quart1 = ds[col].quantile(0.25)
    quart3 = ds[col].quantile(0.75)
    IQR = quart3-quart1
    low_val = quart1-(1.5*IQR)
    high_val = quart3+(1.5*IQR) 
    ds = ds.loc[(ds[col]<low_val) | (ds[col]>high_val)]
    return ds 

def find_Inliers(ds,col) :
    quart1 = ds[col].quantile(0.25)
    quart3 = ds[col].quantile(0.75)
    IQR = quart3-quart1
    low_val = quart1-(1.5*IQR)
    high_val = quart3+(1.5*IQR) 
    ds = ds.loc[(ds[col]>=low_val) & (ds[col]<=high_val)]
    return ds 


df = pd.read_csv("/home/yash/Desktop/Yash /Python2/pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/auto-mpg.csv")

((find_outliers(df,'acceleration')))
((find_Inliers(df,'acceleration')))

((find_outliers(df,'mpg')))
((find_Inliers(df,'mpg')))


# values2 = [3,8,9,2,1,2,4,7,6,6]
# plt.plot(find_Inliers(df,'cylinders')['cylinders'],find_Inliers(df,'cylinders')['weight'])
# plt.plot(find_outliers(df,'cylinders')['cylinders'],find_outliers(df,'cylinders')['weight'])
# plt.plot(range(1,11),values2)
plt.scatter( range(0,find_outliers(df,'acceleration')['acceleration'].__len__()), find_outliers(df,'acceleration')['acceleration'])
# plt.show()
plt.scatter(range(0,find_Inliers(df,'acceleration')['acceleration'].__len__()) , find_Inliers(df,'acceleration')['acceleration'])
plt.show()

# for save it 
# plt.savefig('name.png',format="png")


# show incomin aera whe incom is grater then expensis and when iincoom is less and equal to expensis and fill the area with red color 

