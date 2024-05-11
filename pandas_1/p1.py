import pandas as pd
import random

# print(pd.__version__)

 
xyz =  lambda  n,range_1=0,range_2=10 : ([ random.randint(range_1,range_2)  for i in  (range(len(n)) if type(n)!=type(0) else range(n))])

l = (1,2,3,5)
# print([*xyz(l,50)])
# print(pd.Series(l,index=[*xyz(l,50)]))


data = {'firat1': xyz(10,30,90),'firat2': xyz(10,30,90)}
data_frame = pd.DataFrame(data)

print(data_frame.loc[[0,2,4]])
print(data_frame.loc[0])
print(data_frame.loc[[0]])

print()


# xyz([20],0,11000)



