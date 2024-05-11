import numpy as np 
import matplotlib.pyplot as plt

# x = range(1,6)
# y1 = [1,4,6,8,9]
# y2 = [2,2,7,10,12]
# y3 = [2,8,5,10,6]
# plt.stackplot(x,y1,y2,y3,labels=['A','B','C'],colors=['red','blue','green'])
# plt.legend()
# plt.show()



import pandas  as pd
from pywaffle import Waffle 


data = {
    'phone' : ['xiomi','samsung','apple','Nokia','Realme']
    ,'stock' : [44,12,8,5,50]
}

df = pd.DataFrame(data)
fig = plt.figure(FigureClass=Waffle,rows=10,values = df['stock'],labels=list(df.phone))
plt.show()