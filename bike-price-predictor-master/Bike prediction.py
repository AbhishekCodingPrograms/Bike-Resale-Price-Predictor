#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# get_ipython().run_line_magic('matplotlib', 'inline')
# In[2]:


ddir = r"."

# In[3]:


dt_pt = os.path.join(ddir,'Used_Bikes.csv')


# In[33]:


df = pd.read_csv(dt_pt)
df


# In[34]:


df['brand'].value_counts()


# In[7]:


df['power'].value_counts()


# In[ ]:





# In[ ]:





# In[6]:


df.sample()


# In[7]:


df['bike_name'].sample()


# In[8]:


df['bike_name'].nunique()


# In[9]:


df.info()


# In[10]:


df[df['city'] == 'Delhi']


# In[35]:


original_df = df.copy()


# In[36]:


#df = original_df


# In[37]:


list_city = df['city'].value_counts()[:23].index
list_city


# In[38]:


df['city'] = df['city'].apply(lambda x : x if x in list_city else 'Other')


# In[12]:


df['city'].value_counts()


# In[17]:


sns.catplot(x = 'price', y = 'city', data = df, kind = 'bar')


# In[39]:


df.drop('bike_name',axis = 1, inplace = True)


# In[40]:


df


# In[22]:


df.describe()


# In[101]:


df.head()


# In[23]:


sns.catplot(x = 'kms_driven', kind = 'box', data = df)


# In[24]:


sns.catplot(x = 'age', kind = 'box', data = df)


# In[25]:


sns.catplot(x = 'power', kind = 'box', data = df)


# In[26]:


df.describe()


# In[24]:


def Min_Max_IQR(df, col) :     
    Q1 = np.percentile(df[col], 25)
    Q3 = np.percentile(df[col], 75)
    IQR = Q3 -  Q1
    min_pw = Q1 - 1.5 * IQR
    max_pw = Q3 + 1.5 * IQR
    return min_pw, max_pw


# In[25]:


Min_Max_IQR(df,'age')


# In[26]:


df.shape


# In[27]:


df = df[ (df['age'] >= -2.5) & (df['age'] <= 17.5) ]


# In[28]:


df.shape


# In[29]:


sns.catplot(x = 'age', kind = 'box', data = df)


# In[30]:


df.sample()


# In[31]:


Min_Max_IQR(df, 'kms_driven')


# In[32]:


df = df[ (df['kms_driven'] >= -22500.0) & (df['kms_driven'] <= 69500.0) ]


# In[33]:


df.shape


# In[34]:


sns.catplot(x = 'kms_driven', kind = 'box', data = df)


# In[35]:


Min_Max_IQR(df, 'power')


# In[36]:


df = df[ (df['power'] >= 45) & (df['power'] <= 400) ]
df.shape


# In[37]:


sns.catplot(x = 'power', kind = 'box', data = df)


# In[38]:


df.describe()


# In[39]:


df.sample(5)


# In[40]:


df.info()


# In[41]:


df['age'].value_counts()


# In[53]:


# sns.catplot(x = 'price', y = 'age', data = temp, kind= 'bar')


# In[13]:


df


# In[41]:


df.reset_index(drop=True, inplace = True )


# In[42]:


df


# In[43]:


type_brand = df['brand'].value_counts()[:8].index
type_brand


# In[44]:


df['brand'] = df['brand'].apply(lambda x : x if x in type_brand else 'Other')


# In[45]:


df['brand'].value_counts()


# In[26]:


original_df['brand'].value_counts()


# In[53]:


df.sample(5)


# In[54]:


df['owner'].value_counts()


# In[46]:


# df['owner'].apply(lambda x : x if x == 'First Owner' else 'Second Owner Or More').value_counts()
df.drop('owner', axis = 1, inplace = True)


# In[47]:


df


# In[30]:


df[['city', 'brand']].nunique()


# In[48]:


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split


# In[49]:


df.sample()


# In[50]:


y = df['price']
X = df[['brand', 'kms_driven', 'power', 'age', 'city']]
X


# In[57]:


X['power'].max()


# In[ ]:





# In[66]:


y


# In[58]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


# In[59]:


X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[61]:


X.head()


# In[62]:


trf1 = ColumnTransformer([
    ('ohe', OneHotEncoder(sparse=False, drop='first'), [0, 4])
    # ('orde2', OrdinalEncoder(categories=[['17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1']]), [5])
], remainder='passthrough')


# In[63]:


trf2 = ColumnTransformer([
    ('ss', StandardScaler(), [1, 2, 3])
], remainder='passthrough')


# In[64]:


# orde = OrdinalEncoder()
# orde.categories
# X.iloc[:,6].values.reshape(X.shape[0],1).shape
# orde.fit_transform(X.iloc[:,4].values.reshape(X.shape[0],1))


# In[65]:


X_train.shape, np.sqrt(X_train.shape[0]), np.log2(X_train.shape[0])


# In[66]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor


# In[67]:


from sklearn.metrics import r2_score


# In[68]:


lr = LinearRegression()
rf = RandomForestRegressor()
svm = SVR(kernel='rbf')
knn = KNeighborsRegressor(n_neighbors=5)

#svm_poly3 = SVR(kernel='poly', degree=3)
# svm_poly2 = SVR(kernel='poly', degree=2)
#svm_poly2 = SVR(kernel='sigmoid')
#knn_sqrt = KNeighborsRegressor(n_neighbors=163)
#knn_log2 = KNeighborsRegressor(n_neighbors=14)


# In[69]:


pipe_lr = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('lr', lr)
])

pipe_rf = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('rf', rf)
])

pipe_svm = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('svm', svm)
])

pipe_knn = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('knn', knn)
])


# In[70]:


# pipe_lr.fit(X_train, y_train)
pipe_rf.fit(X_train, y_train)
# pipe_svm.fit(X_train, y_train)
# pipe_knn.fit(X_train, y_train)


# In[75]:


# y_pred_lr = pipe_lr.predict(X_test)
y_pred_rf = pipe_rf.predict(X_test)
# y_pred_svm = pipe_svm.predict(X_test)
# y_pred_knn = pipe_knn.predict(X_test)


# In[76]:


# print(r2_score(y_test, y_pred_lr))
print(r2_score(y_test, y_pred_rf))
# print(r2_score(y_test, y_pred_svm))
# print(r2_score(y_test, y_pred_knn))


# In[77]:


pipe_rf


# In[78]:


y_pred_rf_tr = pipe_rf.predict(X_train)


# In[79]:


print(r2_score(y_train, y_pred_rf_tr))


# In[84]:


from sklearn.model_selection import GridSearchCV


# In[85]:


params = {
    'rf__n_estimators' : [30, 40, 50, 60, 100],
    'rf__max_depth' : [4, 5, 6, 7, None],
}


# In[86]:


grid = GridSearchCV(pipe_rf, params, cv=5)


# In[87]:


grid.fit(X_train, y_train)


# In[88]:


grid.best_score_


# In[89]:


grid.best_params_


# In[95]:


rf_final = RandomForestRegressor(n_estimators=40, max_depth=None)


# In[96]:


pipe_rf_final = Pipeline([
    ('trf1', trf1),
    ('trf2', trf2),
    ('rf_final', rf_final)
])


# In[97]:


pipe_rf_final.fit(X_train, y_train)


# In[100]:


pred_rf_final = pipe_rf_final.predict(X_test)


# In[101]:


r2_score(y_test, pred_rf_final)


# In[81]:


import pickle


# In[82]:


# pickle.dump(pipe_rf_final, open('bike_predictor.pkl', 'wb'))
with open('bike_predictor_rf.pkl', 'wb') as rff : 
    pickle.dump(pipe_rf, rff)


# In[105]:


with open('bike_predictor_lr40.pkl', 'wb') as lff40 : 
    pickle.dump(pipe_rf_final ,lff40)


# In[106]:


X.sample()


# In[107]:


X_test.values[0]


# In[108]:


ch = df.sample(3)
ch


# In[123]:


ch.values


# In[ ]:





# In[126]:


pipe_rf_final.predict([['Royal Enfield', 'Royal Enfield Bullet Electra', 350, 20000.0,'First Owner', '4', 'Delhi']])


# In[130]:


X.sample()


# In[109]:


type_brand = X_train['brand'].unique()


# In[110]:


type_brand


# In[ ]:





# In[111]:


list_city = X_train.city.unique()


# In[112]:


list_city


# In[113]:


search_dic = {
    'brand' : type_brand,
    'city' : list_city
}
search_dic


# In[114]:


with open('search.pkl', 'wb') as sf :
    pickle.dump(search_dic,sf)


# In[116]:


X_test.sample()


# In[156]:


# !pip install streamlit


# In[ ]:




