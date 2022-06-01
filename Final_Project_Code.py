#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
get_ipython().run_line_magic('whos', '')


# In[13]:


sleep_data = pd.read_csv('BILD 62 PROJ/Datasets/Marqueze.csv',sep=',')
sleep_data.head()


# In[15]:


row_index = 'id'
sleep_data = gene_df.set_index(row_index)
sleep_data.head()


# In[ ]:




