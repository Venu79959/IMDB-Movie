#!/usr/bin/env python
# coding: utf-8

# # IMDB Movie Dataset Analysis by KODI VENU

# In[2]:


import pandas as pd
import numpy as np
data = pd.read_csv('IMDB-Movie-Data.csv')


# Displaying Top 10 Rows of the Dataset

# In[3]:


data.head(10)


# Displaying Last 10 Rows of the Dataset

# In[9]:


data.tail(10)


# Finding shape of the Dataset

# In[5]:


data.shape


# In[6]:


print("Number of rows", data.shape[0])
print("Number of columns", data.shape[1])


# Dataset Information

# In[7]:


data.info()


# Checking Missing Values in the dataset

# In[10]:


data.isnull()


# In[11]:


data.isnull().sum()


# In[15]:


import seaborn as sns
sns.heatmap(data.isnull())
import matplotlib.pyplot as plt
plt.show()


# In[16]:


per_missing=data.isnull().sum()*100/len(data)
per_missing


# Dropping Missing Values in the Dataset

# In[17]:


data.dropna(axis=0)


# Checking for Duplicate Data

# In[18]:


dup_data=data.duplicated().any()


# In[19]:


print(dup_data)


# In[20]:


data=data.drop_duplicates()
data


# Dataset Overall Statistics

# In[21]:


data.describe(include='all')


# Displaying the Title of Movie having runtime greater than or equal to 180 Minutes

# In[22]:


data.columns


# In[23]:


data['Runtime (Minutes)']>= 180


# In[24]:


data[data['Runtime (Minutes)']>= 180]


# In[25]:


data[data['Runtime (Minutes)']>= 180]['Title']


# In which year there was the highest average voting?

# In[26]:


data.columns


# In[27]:


data.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[28]:


sns.barplot(x='Year',y='Votes',data=data)
plt.title('Votes by year')
plt.show()


# In which year there was the highest average revenue?

# In[30]:


data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[31]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)
plt.title('Revenue by year')
plt.show()


# Finding the average rating for Each Director

# In[32]:


data.columns


# In[33]:


data.groupby('Director')['Rating'].mean()


# In[34]:


data.groupby('Director')['Rating'].mean().sort_values(ascending=False)


# Displaying the Top 10 lengthy movies title and runtime

# In[35]:


data.columns


# In[36]:


data.nlargest(10,'Runtime (Minutes)')


# In[37]:


data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]


# Displaying number of movies per year

# In[38]:


data.columns


# In[40]:


data['Year'].value_counts()


# In[42]:


sns.countplot(x='Year',data=data)
plt.title('Number of Movies Per Year')
plt.show()


# Finding the most popular movie title (Highest Revenue)

# In[43]:


data.columns


# In[45]:


data['Revenue (Millions)'].max()


# In[48]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]


# In[49]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']


# Displaying the Top 10 Highest Rated Movie Titles and its Directors

# In[50]:


data.columns


# In[53]:


data.nlargest(10,'Rating')[['Title','Rating','Director']]


# Displaying the Top 10 Highest Revenue Movie Titles

# In[54]:


data.columns


# In[55]:


data.nlargest(10,'Revenue (Millions)')


# In[56]:


data.nlargest(10,'Revenue (Millions)')['Title']


# In[57]:


data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']]


# Assigning title as index column

# In[59]:


top_10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].\
set_index('Title') 


# In[60]:


top_10


# In[62]:


sns.barplot(x='Revenue (Millions)',y=top_10.index,data=top_10)
plt.title("Top 10 highest revenue movies")
plt.show()


# Finding the average rating of Movies Year Wise

# In[63]:


data.columns


# In[64]:


data.groupby('Year')['Rating'].mean()


# In[65]:


data.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# Does Rating Affect the Revenue?

# In[66]:


data.columns


# In[67]:


sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)


# Classify movies based on ratings (excellent, good and average)

# In[68]:


data.columns


# In[69]:


def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
        return "Average"


# In[70]:


data['rating_cat'] = data['Rating'].apply(rating)


# In[71]:


data.head()


# count number of action movies

# In[72]:


data.columns


# In[73]:


data['Genre'].dtype


# In[74]:


data['Genre'].str.contains('Action')


# In[75]:


data['Genre'].str.contains('Action',case=False)


# In[76]:


len(data[data['Genre'].str.contains('Action')])


# Find unique values from genre

# In[77]:


data.columns


# In[78]:


data['Genre']


# In[79]:


list1=[]
for value in data['Genre']:
    list1.append(value.split(','))


# In[80]:


list1


# In[81]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[82]:


one_d


# In[84]:


uni_list=[]
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)


# In[85]:


uni_list


# In[86]:


len(uni_list)


# How many films of each genre were made?

# In[87]:


data.columns


# In[88]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[89]:


one_d


# In[94]:


from collections import counter


# In[92]:


counter(one_d)


# In[ ]:




