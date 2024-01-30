#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Identify the distribution of data in the dataset.
# 
# -   Identify outliers in the dataset.
# 
# -   Remove outliers from the dataset.
# 
# -   Identify correlation between features in the dataset.
# 

# * * *
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[18]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[19]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[20]:


# your code goes here
import pandas as pd
import seaborn as sns
#plot distribution curve
df['ConvertedComp'].plot(kind='density')
plt.title('Distribution of Annual salary in USD')
plt.xlabel('Annual Salary in USD')
plt.ylabel('Density')
plt.show()



# Plot the histogram for the column `ConvertedComp`.
# 

# In[21]:


# your code goes here
import pandas as pd
import matplotlib.pyplot as plt

# Plot a histogram of the ConvertedComp column
plt.hist(df['ConvertedComp'], bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Annual Compensation (USD)')
plt.ylabel('Frequency')
plt.title('Histogram of Annual Compensation')
plt.show()


# What is the median of the column `ConvertedComp`?
# 

# In[22]:


# your code goes here
med_ccomp = df['ConvertedComp'].median()
med_ccomp


# How many responders identified themselves only as a **Man**?
# 

# In[23]:


# your code goes here
man_only = df[df['Gender'] =='Man']
print(len(man_only))


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[24]:


# your code goes here
women_only = df[df['Gender']=='Woman']
med_women = women_only['ConvertedComp'].median()
med_women


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[25]:


# your code goes here
min_val = df['Age'].min()
q1_val = df['Age'].quantile(0.25)
med_val = df['Age'].median()
q3_val = df['Age'].quantile(0.75)
max_val = df['Age'].max()

print('Minimum:',min_val)
print('First Quartile',q1_val)
print('Median',med_val)
print('Third Quartile',q3_val)
print('Maximum',max_val)


# Plot a histogram of the column `Age`.
# 

# In[26]:


# your code goes here
df['Age'].plot(kind='hist')
plt.title('Histogram of Responders Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[28]:


# your code goes here
df.boxplot(column =['ConvertedComp'],grid=False) 


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[29]:


# your code goes here
q1 = df['ConvertedComp'].quantile(0.25)
q3 = df['ConvertedComp'].quantile(0.75)
iqr = q3-q1
print(iqr)


# Find out the upper and lower bounds.
# 

# In[31]:


# your code goes here
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print('upper bound: ', upper_bound)
print('lower_bound: ', lower_bound)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[32]:


# your code goes here
outliers = df[(df['ConvertedComp'] < lower_bound) | (df['ConvertedComp'] > upper_bound)]
no_outliers = len(outliers)
print('Outliers Total: ',no_outliers)


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[33]:


# your code goes here
df_cleaned = df[(df['ConvertedComp'] >= lower_bound) & (df['ConvertedComp']<= upper_bound)]
df_cleaned


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[34]:


# your code goes here
correlations = df.corr()['Age']
print(correlations)


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
