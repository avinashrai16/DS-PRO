#!/usr/bin/env python
# coding: utf-8

# ## Comprehensive-Data-Analysis
# 
# New notebook

# In[12]:


import pandas as pd
pd.set_option('display.max_columns', None) # display all the columns in the data frame


# Load data into pandas DataFrame from "/lakehouse/default/" + "Files/Prohance/SUTHGL/Comprehensive/SUTHGL_Comprehensive_Activity_2024-03-15_07-43-45.csv"
df = pd.read_csv("C:\\Users\\raiavina1\\PycharmProjects\\DS-PRO\\Extra-Learning\\SUTHGL_Comprehensive_Activity_2024-03-15_07-43-45.csv")

def has_hours_greater_than_24(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours > 24

# updating zero to a proper time format
#df['Report Columns.TOT_Productive_TOS'] = df['Report Columns.TOT_Productive_TOS'].replace('0',"00:00:00")

print("before drop," ,df.shape)


# remove all the rows which has TOT_Productive_TOS as zero
df.drop(df[df['Report Columns.TOT_Productive_TOS'] == '0'].index,inplace=True)

# remove all the rows which has TOT_Productive_TOS greater than 24
len(df[df['Report Columns.TOT_Productive_TOS'].apply(has_hours_greater_than_24)].index)

df.drop(df[df['Report Columns.TOT_Productive_TOS'].apply(has_hours_greater_than_24)].index,inplace=True)
print("after drop," ,df.shape)

df.head()


# In[13]:


# update object type to date time for the required column
df['Report Columns.TOT_Productive_TOS'] = pd.to_datetime(df['Report Columns.TOT_Productive_TOS'], format='%H:%M:%S').dt.time

df['Report Columns.TOT_Productive_TOS_hour'] = pd.to_datetime(df['Report Columns.TOT_Productive_TOS'], format='%H:%M:%S').dt.hour

# chk the element type for each as the dtype will be object even if the item is of datetime.time
# element_types = df['Report Columns.TOT_Productive_TOS'].apply(type)
# (element_types.unique())

# print(type(df['Report Columns.TOT_Productive_TOS']))


# In[14]:


# adding a target column based on Report Columns.TOT_Productive_TOS if the value is greater than
def setProductiveFlag(date_time):
    # hours, minutes, seconds = map(int, str(date_time).split(':'))
    hours = date_time.hour
    if hours >= 8:
        return 1 # productive
    else:
        return 0 # non productive

target = df['Report Columns.TOT_Productive_TOS'].apply(setProductiveFlag)

type(target)

df['target'] = target


# In[15]:


df.head()


# In[16]:


df.dtypes


# In[17]:


df.head()


# In[18]:


# adding only one column 'Report Columns.TOT_Productive_TOS_hour' as my independent variable i.e X
X =df[["Report Columns.TOT_Productive_TOS_hour"]]
print(type(X))

# setting up target variable (productive non productive) i.e. y
y = df['target']
print(type(y))


# In[19]:


X.shape ,y.shape


# In[20]:


# split the dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)


# In[21]:


X_test


# In[22]:


X_train.shape,X_test.shape


# In[23]:


y_train.shape, y_test.shape


# In[24]:


y_train


# In[25]:


from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier


# In[26]:


classifier.fit(X_train, y_train)


# In[27]:


y_pred = classifier.predict(X_test)
y_pred 
# result is as classification 0 ,1 skit learn has cut off is 0.5 by default


# In[28]:


(X_test)


# In[29]:


classifier.predict_proba(X_test) # below is showing the probability of both classes ( Porductive and non productive)


# In[30]:


# evaluation metrics

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


# In[31]:


confusion_matrix(y_test,y_pred)
# below is the confusion matrix


# In[32]:


accuracy_score(y_test,y_pred)


# In[33]:


print(classification_report(y_test,y_pred))


# In[34]:


from sklearn.metrics import roc_curve,auc,roc_auc_score
import matplotlib.pyplot as plt
y_pred_proba = classifier.predict_proba(X_test)[:,1]
y_pred_proba


# In[35]:


fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)


# In[36]:


roc_auc = auc(fpr, tpr)
print(roc_auc)


# #### Testing for new dataset

# In[37]:


data = {
    'Report Columns.TOT_Productive_TOS_hour': [5,9,2,10]
}
X_test_newdata = pd.DataFrame(data)

type(X_test_newdata)
print(X_test_newdata)


# In[38]:


classifier.predict(X_test_newdata)


# In[39]:


# save my model as pkl file

import pickle as pickle
pickle.dump(classifier,open("classifier_model.pkl","wb"))
pickle.dump(X_test_newdata,open("X_test_newdata.pkl","wb"))

