#!/usr/bin/env python
# coding: utf-8

# In[109]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sn 


# In[110]:


d1=pd.read_csv(r'D:\downloads\Dataset.csv')


# In[111]:


print(d1)


# In[112]:


## data cleaning


# In[113]:


d1 =d1.replace('��','I', regex=True)
d1 =d1.replace('�_','a', regex=True)
d1 =d1.replace('�','A', regex=True)
print(d1)


# In[114]:


### level 3 task 1
### Task: Restaurant Reviews
### Analyze the text reviews to identify the most common positive and negative keywords.


# In[115]:


print("the available words in review text range are: ")
print(d1['Rating text'].value_counts())
print("\n")
print("positive_keywords = ['Good','Very Good','Excellent']")
print("negative_keywords = ['Poor']")
print("neutal_keywords = ['Average','Not rated']")
print("\n")
a = (d1['Rating text'] == 'Good').sum()
b = (d1['Rating text'] == 'Poor').sum()
print("therefore the most common positive keyword will be 'Good':",a)
print("therefore the most common negative keyword will be 'Poor':",b)






# In[116]:


### Calculate the average length of reviews and explore if there is a relationship between review length and rating.


# In[117]:


res = sum(map(len, d1['Rating text']))/(len(d1['Rating text']))
print("The Average length of review in review text list is : ", str(res))


# In[118]:


d1["Review Length"]= d1["Rating text"].str.len() 
d1


# In[119]:


corr=d1['Review Length'].corr(d1['Aggregate rating'])
print("relationship between review length and rating. :",corr)


# In[120]:


## level 3 task 2
## Task: Votes Analysis

##Identify the restaurants with the highest and lowest number of votes.


# In[121]:


max_votes = d1['Votes'].max()
r = d1.loc[d1['Votes'] == max_votes, 'Restaurant Name']

print("Restaurant with maximum votes:", r)
print("no. of votes recieved : ",max_votes)


# In[122]:


min_votes = d1['Votes'].min()
r1 = d1.loc[d1['Votes'] == min_votes, 'Restaurant Name']

print("Restaurant with minimum votes:", r1)
print("no. of votes recieved : ",min_votes)


# In[123]:


## Analyze if there is a correlation between the number of votes and the rating of a restaurant. 


# In[124]:


corr = d1['Votes'].corr(d1['Aggregate rating'])
print ("Correlation between the number of votes and the rating of a restauran: ", corr)


# In[125]:


## level 3 task 3
## Analyze if there is a relationship between the price range and the availability of online delivery and table booking.


# In[126]:


d2 = d2.replace({'Has Table booking': {'Yes': 1,'No': 0}}) 
d2 = d2.replace({'Has Online delivery': {'Yes': 1,'No': 0}}) 

print(d2)


# In[127]:


corr=d2['Price range'].corr(d2['Has Table booking'])
print("relationship between the price range and table booking :",corr)
corr=d2['Price range'].corr(d2['Has Online delivery'])
print("relationship between the price range and the availability of online delivery",corr)


# In[128]:


### Determine if higher-priced restaurants are more likely to offer these services.


# In[129]:


df=d2.sort_values("Average Cost for two", ascending=False)
dt=df.head(100)
print(dt)


# In[130]:


per = dt['Has Table booking'].sum()
print("the percentage of table booking in top 100 high priced restaurants is : ",per*100/100)
print("Therefore 58% top 100 high priced restaurants provide table booking service.")


# In[131]:


per1 = dt['Has Online delivery'].sum()
print("the percentage of table booking in top 100 high priced restaurants is : ",per1*100/100)
print("Therefore none among the top 100 high priced restaurants provide online delivery service.")


# In[ ]:




