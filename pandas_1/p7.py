# # from wordcloud import WordCloud ,STOPWORDS

# # from matplotlib import pyplot as plt


# # stopwords =  set(STOPWORDS)
# # print(stopwords)

# # with open(r'/home/yash/Desktop/Yash /Python2/pg11.txt') as f :
# #     alice_novel = f.read()
# # stopwords.add('said')
# # stopwords.add('alice')
# # alic_w = WordCloud(background_color='white',max_words=2000,stopwords=stopwords)
# # alic_w.generate(alice_novel)
# # plt.imshow(alic_w)
# # plt.axis('off')
# # plt.show()


# import seaborn as sns 
# import pandas as pd 
# from matplotlib import pyplot as plt


# dataset = pd.read_csv("pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/auto-mpg.csv");
# sns.regplot(x='mpg',y='acceleration',data=dataset)
# plt.show()


# print(dataset.corr(numeric_only=True))




import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = np.random.randint(low=1,high=100,size=(10,10))

print(data)
hm = sns.heatmap(data=data,vmin=20,vmax=100 ,annot=True)
plt.show()