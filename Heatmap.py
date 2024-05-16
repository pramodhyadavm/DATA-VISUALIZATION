#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt
data = np.random.random((13, 16 ))
plt.imshow( data,cmap="magma")
plt.title( "2-D Heat Map")
plt.colorbar()
plt.show()


# In[2]:


#Program to plot 2-D Heat map
#using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt
data = np.random.random((12,12))
plt.imshow(data, cmap='autumn')
plt.title("Heatmap with different color")
plt.show()


# In[3]:


# importing the modules
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# generating 2-D 10x10 matrix of random numbers
# from 1 to 100
data = np.random.randint(low=14,high=100,size=(10,10))
#plotting the heatmap
hm = sns.heatmap(data=data,annot=True)
#displaying the potted heatmap
plt.show()


# In[ ]:
