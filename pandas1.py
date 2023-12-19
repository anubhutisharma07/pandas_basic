#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


np.arange(0,20).reshape(5,4)


# In[12]:


#creating dataframe 


# In[18]:


df=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["r1","r1","r3","r4","r5"],columns=["c1","c2","c3","c4"])


# In[19]:


df


# In[21]:


df.head(3)                        ##showing starting 3 records


# In[23]:


df.tail(2)                                   ##showing last row recods


# In[24]:


type(df)                       ##pandas is a data structure


# In[25]:


df.info()                   ##for presenting col's data type


# In[26]:


##Indexing == there are three type of technic we use in indexing
## 1.) colmnname - by using col name, When we use this we got col information only
## 2.) rowindex - by using "[loc]" in-built function
## 3.) rowindex and columnindex number - by using "[.iloc]" in-built function


# In[27]:


## type 1.) colmnname
df.head()


# In[28]:


df["c1"]             ##for single column value


# In[29]:


df[["c1","c4","c2"]]            ##for multiple value


# In[30]:


##different series and dataframe 


# In[31]:


type(df["c1"])


# In[32]:


type(df[["c2","c1","c4"]])


# In[33]:


##series have only one single row and col 
##dataframe have multiple rows and cols


# In[34]:


##type 2.) rowindex


# In[36]:


df.loc["r3"]                                 ##for single row printing 


# In[37]:


df.loc[["r1","r4","r3"]]                           ##for multiple row printing 


# In[38]:


##type 3.) rowindex number and columnname number 


# In[39]:


df.head()


# In[40]:


df.iloc[2:4,1:4]


# In[ ]:


##converting dataframe into array


# In[45]:


df.iloc[:,:].values


# In[ ]:




