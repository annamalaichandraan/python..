#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hyy")


# In[2]:


import numpy as np


# In[3]:


np.linspace(1,20,5)


# In[4]:


np.linspace(0,5,5)


# In[6]:


np.linspace(1,10,5)


# In[7]:


np.random.rand(1,10)


# In[8]:


np.random.randn(1,10)


# In[9]:


np.random.randint(10,20)


# In[10]:


np.random.rand(1,100,10)


# In[11]:


np.random.rand(1,10,20)


# In[12]:


np.random.rand(1,10,5)


# In[13]:


np.random.rand(1,20,1)


# In[14]:


np.random.rand(1,20,5)


# In[15]:


np.random.randint(1,2,5)


# In[16]:


np.random.rand(1,2,5)


# #### uniform distribution "rand" key varies from 0 to 1

# In[17]:


np.random.rand(3,2)


# ### normal distribution where "randn" key values tends to negative values 

# In[18]:


np.random.randn(3,2)


# In[19]:


np.random.randint(34,100)


# In[20]:


np.random.randint(34,100,50)


# In[21]:


sample_array=np.arange(30)
sample_array


# In[23]:


rand_array=np.random.randint(0,100,20)
rand_array


# In[24]:


sample_array.reshape(6,5)


# In[26]:


sample_array.reshape(3,10)


# In[27]:


rand_array.min()


# In[28]:


rand_array.max()


# In[29]:


sample_array.min()


# In[30]:


sample_array.max()


# In[31]:


sample_array=np.random.randint(0,100,20)
sample_array


# In[32]:


rand_array=np.arange(30)
rand_array


# In[33]:


rand_array.min()


# In[34]:


rand_array.max()


# In[35]:


sample_array.min()


# In[36]:


sample_array.max()


# ## argmin - index of the minimum value

# In[37]:


rand_array.argmin()


# In[38]:


sample_array.argmin()


# In[39]:


sample_array.argmin()


# In[42]:


np.eye(3)


# In[43]:


np.eye(5)


# In[44]:


a=np.eye(5)
a


# In[45]:


a=np.random.rand(3,2)
a


# ### transpose

# In[46]:


a.T


# In[47]:


sample_array=np.random.rand(10,21)
sample_array


# In[48]:


sample_array=np.arange(10,21)
sample_array


# In[49]:


sample_array[3]


# In[50]:


sample_array[5]


# In[51]:


sample_array[3:7]


# In[52]:


sample_array[1:4]


# In[53]:


sample_array[0:4]


# In[55]:


sample_array[1:4]=100
sample_array


# In[56]:


sample_array=np.arange(10,21)
sample_array


# In[58]:


sample_array=np.arange(30,40)
sample_array


# In[59]:


sample_array[1]=4
sample_array


# In[60]:


sample_array[0:7]


# In[61]:


sample_array[2:4]=5
sample_array


# In[62]:


sample_array=np.arange(10,21)
sample_array


# In[63]:


sample_array[0:7]


# In[64]:


subset_sample_array=sample_array[0:7]
sample_array


# In[65]:


subset_sample_array=sample_array[0:7]
subset_sample_array


# In[66]:


subset_sample_array[1:4]=1001
subset_sample_array


# ### : indicates all

# In[67]:


subset_sample_array[:]=1001
subset_sample_array


# ### two dimensional array

# In[68]:


import numpy as np


# In[70]:


sample_matrix=np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8]])
sample_matrix


# # rows and columns are allocated in ammaner such that r0,r1 and r2 whwre as the columns are in manner should be c0,c1,c2,c3

# In[72]:


sample_matrix[2][3]


# In[73]:


sample_matrix[2]


# In[74]:


sample_matrix[:,(3,2)]


# In[75]:


sample_matrix[:,(2,3)]


# In[76]:


sample_matrix[:,(3,3)]


# In[77]:


sample_matrix[1][3]


# In[79]:


sample_matrix[2][3]


# In[80]:


sample_matrix[1,3]


# In[81]:


sample_matrix[2,:]


# In[82]:


sample_matrix[:,3]


# In[83]:


sample_matrix[:,2]


# In[84]:


sample_matrix[1,:]


# In[85]:


sample_matrix[0,:]


# In[88]:


sample_matrix[0:2,2]


# In[89]:


sample_matrix[0:2]


# In[90]:


sample_matrix[:]


# In[91]:


sample_matrix[0,2]


# In[92]:


sample_matrix[:,0]


# In[93]:


sample_matrix[1:2]


# In[94]:


sample_matrix[0:1]


# ### numpy also can as use for claculating square varience mean by using different function such that standard deviation mean 

# In[95]:


array=np.random.rand(3,4)
array


# In[96]:


array=np.random.randn(3,4)
array


# In[97]:


np.round(array,decimals=3)


# In[98]:


np.round(array,decimals=2)


# In[ ]:




