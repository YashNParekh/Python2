import pandas as pd

bolly = pd.read_csv('/home/yash/Desktop/Yash /Python2/pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/bollywood.csv')

# print(bolly['lead'])


# # now print the movive in vich Vicky Kaushal hash work 

# print(bolly[bolly['lead']=='Vicky Kaushal'])

# # print only movie name in which Vicky Kaushal hash work

# print(bolly[bolly['lead']=='Vicky Kaushal']['movie'])


#  you need too convert dataframe into sericse with movie name as index and lead char as value

# print(pd.Series(data= bolly['lead'],index=bolly.columns))
bolly1 = pd.read_csv('/home/yash/Desktop/Yash /Python2/pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/bollywood.csv',index_col='movie').squeeze()
# print(type(bolly1))
# print(type(bolly))

# # print the actor work in the file Mantra (2016 film)

# print(bolly[bolly['movie']=="Mantra (2016 film)"]['lead'])
# print(bolly1['Mantra (2016 film)'])


moive1 = pd.read_csv('/home/yash/Desktop/Yash /Python2/pandas_1/dataset/Datasets-20240501T060332Z-001/Datasets/Datasets/Datasets/movies.csv')
print(moive1)

print(moive1.info())
print(moive1.size)
print(1629*18)



# print number of movies with imdb rating is grater then 8 
print(moive1[moive1['imdb_rating']>8].shape[0])


# print title and imdb rating for movies of type drama 
print('hii')
print(moive1[moive1['genres']=='Drama'][['title_x','imdb_rating']])



print(moive1[ (moive1['imdb_rating']>8) & (moive1['imdb_rating']<10)  ].shape[0])



