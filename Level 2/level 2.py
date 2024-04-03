#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[2]:


d1=pd.read_csv(r'D:\downloads\Dataset.csv')


# In[3]:


print(d1)


# In[4]:


## data cleaning


# In[5]:


d1 =d1.replace('��','I', regex=True)
d1 =d1.replace('�_','a', regex=True)
d1 =d1.replace('�','A', regex=True)
print(d1)


# In[6]:


### level 2 task 1
### Task: Restaurant Ratings

##Analyze the distribution of aggregate ratings and determine the most common rating range.


# In[7]:


print(d1[['Aggregate rating']].describe())


# In[8]:


## Calculate the average number of votes received by restaurants.


# In[9]:


k=d1['Votes'].mean()
print("average number of votes received by restaurants. :",k)


# In[10]:


### level 2 task 2
##Task: Cuisine Combination

##Identify the most common combinations of cuisines in the dataset.


# In[11]:


print(d1[['Cuisines']].describe())


# In[12]:


print('most common combinations ofcuisines: ',d1['Cuisines'].value_counts().idxmax())


# In[13]:


###level 2 task 3
##Task: Geographic Analysis

##Plot the locations of restaurants on a map using longitude and latitude coordinates.


# In[14]:


pip install folium


# In[15]:


import folium


# In[16]:


cities = pd.read_csv('D:\downloads\Dataset.csv')
print(cities.shape)
cities.head(3)


# In[17]:


world_all_cities = folium.Map()

for _, city in cities.iterrows():
    folium.Marker(location=[city['Latitude'], city['Longitude']],).add_to(world_all_cities)

world_all_cities


# In[ ]:




