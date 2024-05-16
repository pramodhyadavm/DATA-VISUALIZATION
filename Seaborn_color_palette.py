#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
#Setting a figure size for all the plots we shall be drawing in this kernel:
sns.set(rc={"figure.figsize":(6,6)})


# In[3]:


current_palette = sns.color_palette()
sns.palplot(current_palette)


# In[5]:


sns.palplot(sns.color_palette("hls", 8))


# In[6]:


sns.palplot(sns.color_palette("husl", 8))


# In[9]:


sample_colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple", "pale red", "medium green", "denim blue"]
sns.palplot(sns.xkcd_palette(sample_colors))


# In[10]:


# Default Matplotlib Cubehelix version:
sns.palplot(sns.color_palette("cubehelix", 8))


# In[11]:


# Default Seaborn cubehelix version:
sns.palplot(sns.cubehelix_palette(8))


# In[15]:


# Density plot with Seaborn defaults:
x,y = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=300).T

sample_cmap = sns.cubehelix_palette(light=1, as_cmap=True)
sns.kdeplot(x, y, cmap=sample_cmap, shade=True)


# In[16]:


sns.palplot(sns.cubehelix_palette(n_colors=8, start=1.7, rot=0.2, dark=0, light=.95, reverse=True))


# In[17]:


# Loading up built-in dataset:
tips = sns.load_dataset("tips")

# Creating Strip plot for day-wise revenue:
sns.stripplot(x="day", y="total_bill", data=tips, color="g")


# In[18]:


# Set Theme:
sns.set_style('whitegrid')

# Creating Strip plot for day-wise revenue:
sns.swarmplot(x="day", y="total_bill", data=tips, palette="viridis")


# In[ ]:


iris = sns.load_dataset("iris")

sns.boxplot(x="species", y="petal_length", data=iris, palette="cividis")
