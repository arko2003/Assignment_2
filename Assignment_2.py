#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df=pd.read_csv("C:/Users/SOLO's WORK-IN/Desktop/athlete_events.csv")
df.head()


# In[2]:


#**** name jesse owen is not in data, so checking for Laura Gabriela event in which he won a medal*** 


# In[8]:


Name= df[df.Name =="Laura Gabriela Crlescu-Badea"]


# In[36]:


df[df.Event.str.contains('100 metres')]


# In[12]:


df.head(10)


# In[21]:


df['NOC'][df.Event =="Badminton Men's Singles"][df.Medal == "Gold"].value_counts()


# In[28]:


df.sort_values(by="Name", ascending=True)


# In[37]:


df["Name"][df.Event == "Athletics Men's 100 metres"][df.Sex == "M"][df.Medal == "Gold"]


# In[ ]:




