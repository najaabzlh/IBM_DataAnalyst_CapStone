#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Wrangling Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be performing data wrangling.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Identify duplicate values in the dataset.
# 
# -   Remove duplicate values from the dataset.
# 
# -   Identify missing values in the dataset.
# 
# -   Impute the missing values in the dataset.
# 
# -   Normalize data in the dataset.
# 

# <hr>
# 

# ## Hands on Lab
# 

# Import pandas module.
# 

# In[2]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[20]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")
df.shape


# ## Finding duplicates
# 

# In this section you will identify duplicate values in the dataset.
# 

#  Find how many duplicate rows exist in the dataframe.
# 

# In[7]:


# your code goes here
duplicate_rows = df.duplicated()
no_duplicate_row = duplicate_rows.sum()
print(no_duplicate_row)


# In[25]:


#get duplicate value columns 'Respondent'
dup_respondent = df['Respondent'].duplicated()
total_dup = dup_respondent.sum()
print(total_dup)


# ## Removing duplicates
# 

# Remove the duplicate rows from the dataframe.
# 

# In[9]:


# your code goes here
df_new = df.drop_duplicates()
df_new.shape


# In[26]:


df_resp_new = df['Respondent'].drop_duplicates()
df_resp_new.shape


# In[27]:


df_Edlevel_new = df['EdLevel'].drop_duplicates()
df_Edlevel_new.shape


# Verify if duplicates were actually dropped.
# 

# In[12]:


# your code goes here
print('Original dataframe shape: ',df.shape)
print('New dataframe after remove duplicate shape: ',df_new.shape)


# ## Finding Missing values
# 

# Find the missing values for all columns.
# 

# In[13]:


# your code goes here
missing_values = df_new.isnull()
print(missing_values)


# Find out how many rows are missing in the column 'WorkLoc'
# 

# In[14]:


# your code goes here
no_missing_val = df_new['WorkLoc'].isnull().sum()
print(no_missing_val)


# In[28]:


blank_EdLevel = df_new['EdLevel'].isnull().sum()   #get missing rows in column EdLevel
print(blank_EdLevel)


# In[29]:


blank_Country = df_new['Country'].isnull().sum()    #get missing rows in column Country
print(blank_Country)


# ## Imputing missing values
# 

# Find the  value counts for the column WorkLoc.
# 

# In[16]:


# your code goes here
val_cnt = df_new['WorkLoc'].value_counts()
print(val_cnt)


# Identify the value that is most frequent (majority) in the WorkLoc column.
# 

# In[17]:


#make a note of the majority value here, for future reference
freq_val = df_new['WorkLoc'].mode()[0]
print(freq_val)


# In[33]:


#get majority category in column Employment
freq_emp = df_new['Employment'].mode()[0]
print(freq_emp)

#get minimum number of rows in UndergradMajor
undergrad_val_cnt = df['UndergradMajor'].value_counts()
min_cat = undergrad_val_cnt.idxmin()
print(undergrad_val_cnt)


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# 

# In[19]:


# your code goes here
df_new['WorkLoc'].fillna(freq_val,inplace=True)


# After imputation there should ideally not be any empty rows in the WorkLoc column.
# 

# Verify if imputing was successful.
# 

# In[21]:


# your code goes here
df_new['WorkLoc'].isnull().sum()    #check if still have missing value, after imputation should not have missing value


# ## Normalizing data
# 

# There are two columns in the dataset that talk about compensation.
# 
# One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
# 
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq". 
# 
# This makes it difficult to compare the total compensation of the developers.
# 
# In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
# 
# Once this column is ready, it makes comparison of salaries easy.
# 

# <hr>
# 

# List out the various categories in the column 'CompFreq'
# 

# In[22]:


# your code goes here
CompFreq_cat = df['CompFreq'].unique()
print(CompFreq_cat)


# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
# 

# Double click to see the **Hint**.
# 
# <!--
# 
# Use the below logic to arrive at the values for the column NormalizedAnnualCompensation.
# 
# If the CompFreq is Yearly then use the exising value in CompTotal
# If the CompFreq is Monthly then multiply the value in CompTotal with 12 (months in an year)
# If the CompFreq is Weekly then multiply the value in CompTotal with 52 (weeks in an year)
# 
# -->
# 

# In[23]:


# your code goes here
df['NormalizedAnnualCompensation'] = df.apply(lambda row: row['CompTotal'] if row['CompFreq']=='Yearly' else row['CompTotal']*12 if row['CompFreq']=='Monthly' else row['CompTotal']*52, axis=1)


# In[24]:


df['NormalizedAnnualCompensation']


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

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
