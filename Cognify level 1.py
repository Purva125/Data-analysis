#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[4]:


d1=pd.read_csv(r'D:\downloads\Dataset.csv')


# In[5]:


print(d1)


# In[6]:


## data cleaning


# In[7]:


d1 =d1.replace('��','I', regex=True)
d1 =d1.replace('�_','a', regex=True)
d1 =d1.replace('�','A', regex=True)
print(d1)


# In[8]:


d1.info()


# In[9]:


x=d1['Aggregate rating'].mean()
print("mean :",x)
y=d1['Aggregate rating'].median()
print("median :",y)
z=d1['Aggregate rating'].mode()
print("mode :",z)


# In[10]:


### level 1 task 1
### Determine the top three most common cuisines in the dataset.


# In[11]:


print("the top three most common cuisines: ")
print(d1['Cuisines'].value_counts().nlargest(3))


# In[12]:


### Calculate the percentage of restaurants that serve each of the top cuisines.


# In[13]:


print("percentage for North Indian : ",(d1['Cuisines'].value_counts()['North Indian'])*100/9551)
print("percentage for North Indian, Chinese : ",(d1['Cuisines'].value_counts()['North Indian, Chinese'])*100/9551)
print("percentage for Chinese : ",(d1['Cuisines'].value_counts()['Chinese'])*100/9551)


# In[14]:


### level 1 task 2
### Identify the city with the highest number of restaurants in the dataset.


# In[15]:


print('city with the highest number of restaurants: ',d1['City'].value_counts().idxmax())
print("the count of restaurants is: ",(d1['City'].value_counts()['New Delhi']))


# In[16]:


### Calculate the average rating for restaurants in each city.


# In[17]:


d2 = d1.groupby(['City']).agg({'Aggregate rating':[np.mean]})
print(d2)


# In[18]:


d2.info()


# In[19]:


### Determine the city with the highest average rating.


# In[20]:


list(d2.columns)


# In[21]:


d2=d2.sort_values(('Aggregate rating', 'mean'), ascending=False)
print("Therefore the city with highest average rating is : \n",d2.head(1))


# In[22]:


### level 1 task 3
### Task: Price Range Distribution

### Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.


# In[23]:


## histogram 
d1.hist(column='Price range') 
plt.xlabel('Price range')
plt.ylabel('number of restaurants')
plt.show() 


# In[24]:


### Calculate the percentage of restaurants in each price range category.


# In[25]:


print("the number restaurnats in each price range: ")
print(d1['Price range'].value_counts().nlargest(4))


# In[26]:


print("the percentage of restaurnats in each price range: ")
print(d1['Price range'].value_counts(normalize=True)*100)


# In[27]:


### level 1 task 4
### Task: Online Delivery
### Determine the percentage of restaurants that offer online delivery.


# In[28]:


d2 = d1.replace({'Has Online delivery': {'Yes': 1,'No': 0}}) 
k = d2['Has Online delivery'].sum()
k1 = d2['Has Online delivery'].count()
 
print(" percentage of restaurants that offer online delivery: ",k*100/k1)


# In[29]:


### Compare the average ratings of restaurants with and without online delivery.


# In[30]:


d3 = d1.groupby(['Has Online delivery']).agg({'Aggregate rating':[np.mean]})
print("the average ratings of restaurants with and without online delivery")
print(d3)


# In[ ]:




