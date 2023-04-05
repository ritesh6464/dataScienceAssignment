#!/usr/bin/env python
# coding: utf-8

# ## Assignment-1-Q7 (Basic Statistics Level-1)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


cars=pd.read_csv('C:\\Users\\Ritesh\\Downloads\\Q7.csv')
cars


# In[7]:


# mean
cars.mean()


# In[8]:


# Median
cars.median()


# In[9]:


# Mode
cars.Points.mode() 


# In[10]:


cars.Score.mode()


# In[11]:


# Variance
cars.var()


# In[12]:


# Satndard Deviation
cars.std()


# In[13]:


cars.describe()


# In[14]:


Points_Range=cars.Points.max()-cars.Points.min()
Points_Range


# In[15]:


Score_Range=cars.Score.max()-cars.Score.min()
Score_Range


# In[16]:


Weigh_Range=cars.Weigh.max()-cars.Weigh.min()
Weigh_Range


# In[17]:


f,ax=plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.boxplot(cars.Points)
plt.title('Points')
plt.subplot(1,3,2)
plt.boxplot(cars.Score)
plt.title('Score')
plt.subplot(1,3,3)
plt.boxplot(cars.Weigh)
plt.title('Weigh')
plt.show()


# In[ ]:




