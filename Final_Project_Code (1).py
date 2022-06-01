#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
get_ipython().run_line_magic('whos', '')


# In[18]:


sleep_data = pd.read_csv('BILD 62 PROJ/Datasets/Marqueze.csv',sep=',')
sleep_data.head()


# In[19]:


row_index = 'id'
sleep_data = sleep_data.set_index(row_index)
sleep_data.head()


# In[ ]:




