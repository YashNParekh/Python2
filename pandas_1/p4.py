import pandas as pd 
# from p2 import printx

printx = lambda x : print(x,end='\n\n\n')



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

printx((find_outliers(df,'acceleration')))
printx((find_Inliers(df,'acceleration')))

printx((find_outliers(df,'mpg')))
printx((find_Inliers(df,'mpg')))
