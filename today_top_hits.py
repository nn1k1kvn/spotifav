
# coding: utf-8

# In[27]:


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[41]:

df = pd.read_csv('../Data/todays_top_hits_06032017.csv', sep=',', encoding='utf8')


# In[29]:

df


# In[30]:

#get the last 4 characters from Date xx/xx/xxxx or xxxx for consistency
df['YEAR'] = df['RELEASE'].str[:4]


# In[31]:

df['YEAR'] = df['YEAR'].convert_objects(convert_numeric=True)


# In[32]:

df = df.drop('RELEASE', 1)


# In[33]:

df


# In[34]:

#hack because pandas thinks that our minutes are hours
time = pd.DatetimeIndex(df['LENGTH'])
seconds = time.hour * 60 + time.minute


# In[35]:

(df['Seconds']) = seconds


# In[36]:

df = df.drop('LENGTH', 1)


# In[37]:

df


# In[38]:

df2 = pd.read_pickle('spotify_dataframe.pkl')


# In[39]:

df2


# In[40]:

plt.figure(1, figsize=(20, 10),)

hfont = {'fontname':'Proxima Nova'}

plt.subplot(331)
sns.distplot(df2.BPM);
sns.distplot(df.BPM);
#plt.text(10, .010, r'$\mu=\ 121.12$', fontsize=22)
plt.xlabel('Tempo (BMP)', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(332)
sns.distplot(df2['POP.']);
sns.distplot(df['POP.']);
#plt.text(70, .020, r'$\mu=\ 30.51$', fontsize=22)
plt.xlabel('Popularity', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(333)
sns.distplot(df2.ENERGY);
sns.distplot(df.ENERGY);
#plt.text(85, .010, r'$\mu=\ 52.05$', fontsize=22)
plt.xlabel('Energy', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(334)
sns.distplot(df2.LOUD);
sns.distplot(df.LOUD);
#plt.text(-30, 0.10, r'$\mu=\ -9.36$', fontsize=22)
plt.xlabel('Loudness  ', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(335)
sns.distplot(df2.DANCE);
sns.distplot(df.DANCE);
#plt.text(70, 0.02, r'$\mu=\ 47.38$', fontsize=22)
plt.xlabel('Danceability ', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(336)
sns.distplot(df2.VALENCE);
sns.distplot(df.VALENCE);
#plt.text(80, 0.01, r'$\mu=\ 40.68$', fontsize=22)
plt.xlabel('Valence (positive mood)', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(337)
sns.distplot(df2.ACOUSTIC);
sns.distplot(df.ACOUSTIC);
#plt.text(80, 0.02, r'$\mu=\ 40.46$', fontsize=22)
plt.xlabel('Acousticness', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(338)
sns.distplot(df2.YEAR,).set(yscale="log");
sns.distplot(df.YEAR,).set( yscale="log");
plt.xlabel('Release Year', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(339)
sns.distplot(df2.Seconds);
sns.distplot(df.Seconds);

#this corresponds to YEAR above, but somehow Matplot fucked it up when changing it
#plt.text(-1100, 0.002, r'$\mu≈\ 2004$', fontsize=22)

#Seconds 
#plt.text(500, 0.002, r'$\mu=\ 262.82$', fontsize=22)
plt.xlabel('Song Duration (sec)', fontsize=18, **hfont)
plt.grid(True)

plt.tight_layout(pad=0.5, w_pad=0.6, h_pad=1.0)


# In[ ]:



