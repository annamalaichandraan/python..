#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr=array([1,2,3,4,5,6])
arr


# In[3]:


arr=np.array([1,2,3,4,5,7])
arr


# In[5]:


list_of_list=[[1,2,3,4],[5,6,7],[7,8,9,0]]
matrix=np.array(list_of_list)


# In[6]:


matrix


# In[7]:


pip install numpy


# In[8]:


list_of_list=[[1,2,3,4],[5,6,7],[7,8,9,0]]
matrix=np.array(list_of_list)


# In[9]:


import numpy as np


# In[10]:


a=np.zeros(3)


# In[11]:


a


# In[12]:


type(a)


# In[13]:


type(a[1])


# In[14]:


list_of_list=[[1,2,3],[5,6,7],[7,8,9]]
matrix=np.array(list_of_list)
matrix


# #### numpy list of list should be of same size

# In[15]:


np.arrange(3,10)


# In[16]:


np.arange(3,10)


# In[17]:


np.arange(10)


# In[18]:


np.arange(1,12,6)


# In[19]:


np.arange(1,50,5)


# In[20]:


np.zeros(10)


# In[21]:


np.zeros(4,int)


# In[22]:


np.zeros(2,4,int)


# In[23]:


np.zeros(2,int)


# In[24]:


np.zeros((1,7),int)


# In[25]:


np.zeros((1,100),float)


# In[26]:


np.tows(11)


# In[27]:


np.ones(10)


# In[28]:


np.ones((2,10),int)


# In[29]:


np.ones((1,10),int)


# In[30]:


np.zeros((2,5),int)


# In[31]:


np.ones(2,5)


# In[32]:


np.ones(1,2,int)


# In[33]:


np.ones((1,2),float)


# In[34]:


np.ones((10,10),int)


# In[35]:


np.ones(10)


# In[36]:


np.ones(10,int)


# #### the syntax should be shape ,datatype

# ###### np.sam(shape,datatype)
# ######  shape should consists of starting vale and ending value and the integer type need also be followed

# In[37]:


np.eye(3)


# In[38]:


np.linspace(0,1,5)


# In[39]:


np.linspace((0,1,5),int)


# In[40]:


np.linspace(0,1,4)


# In[41]:


np.arange(10)


# In[42]:


np.linspace(1,10,100)


# In[43]:


np.linspace(1,10,100)


# In[44]:


np.linspace(1,100,10)


# In[45]:


np.linspace((1,100,10),int)


# In[46]:


np.zeors(1)


# In[47]:


np.zeros(10)


# In[48]:


np.zeros(2)


# In[49]:


np.ones(10)


# In[50]:


np.ones((1,10),int)


# In[51]:


list_of_list=[[1,2,3],[2,3,4],[3,4,5]]
matrix=np.arange(list_of_list)
matrix


# In[52]:


list_of_list=[[1,2,3],[2,3,4],[3,4,5]]
matrix=np.array(list_of_list)
matrix


# In[53]:


np.array([1,2,3,3,4])


# In[54]:


np.linspace(0,1,5)


# In[55]:


np.eye(2)


# In[56]:


np.eye(3)


# In[57]:


np.random.rand(3,2)


# In[58]:


np.random.rand(3,3)


# np.random.rand(3,10)

# #### uniform distribution of random numbers 

# In[60]:


np.random.rand(3,2)


# In[62]:


np.random.rand(3,3)


# #### normal distribution

# In[63]:


np.random.randn(3,3)


# #### any integer can randomly generated between 34 to 100 thats the randint will stands for 

# In[64]:


np.random.randint(34,100)


# In[65]:


sample_array=np.arange(30)
sample_array


# In[66]:


rand_array=np.random.randint(0,100,20)
rand_array


# In[68]:


sample_array.reshape(3,10)


# In[69]:


rand_array.min()


# In[70]:


rand_array.max()


# In[71]:


smaple_array.min()


# In[72]:


sample_array.min()


# In[73]:


sample_array.max()


# In[74]:


sample_array.dtype


# In[ ]:




