#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt


# In[60]:


airbnb = pd.read_csv('C:\\Users\\safyc\\Guvi\\Airbnb\\airbnb.csv')
airbnb.head(5)


# In[11]:


airbnb.shape


# In[62]:


airbnb.info()


# In[64]:


airbnb.isnull().sum()


# In[65]:


# Print data types of DataFrame
airbnb.dtypes


# In[66]:


airbnb.info()


# In[67]:


airbnb.isna().sum()


# In[68]:


# Print description of DataFrame
airbnb.describe()


# In[69]:


# Find number of unique values in room_type column
airbnb['room_type'].unique()


# In[70]:


# Doing some sanity checks on date data
today = dt.date.today()
today


# In[71]:


# Are there reviews in the future?
import pandas as pd

# Assuming 'last_review' is a column in the airbnb DataFrame
airbnb['last_review'] = pd.to_datetime(airbnb['last_review'])

# Now you can use the .dt accessor
today = pd.to_datetime('today').date()
airbnb[airbnb['last_review'].dt.date > today]


# In[72]:


# Are there listings in the future?
airbnb['listing_added'] = pd.to_datetime(airbnb['listing_added'])
today = pd.to_datetime('today').date()
airbnb[airbnb['listing_added'].dt.date > today]


# In[73]:


# Are there any listings with listing_added > last_review
inconsistent_dates = airbnb[airbnb['listing_added'].dt.date > airbnb['last_review'].dt.date]
inconsistent_dates


# In[74]:


inconsistent_dates.shape


# In[75]:


# Drop these rows since they are only 6 rows
airbnb.drop(inconsistent_dates.index, inplace = True)


# In[76]:


airbnb.head()


# In[77]:


# Find duplicates
duplicates = airbnb.duplicated(subset = 'listing_id', keep = False)
print(duplicates.sum())


# In[78]:


# Find duplicates
airbnb[duplicates].sort_values('listing_id')


# In[79]:


airbnb = airbnb.drop_duplicates()


# In[80]:


duplicates = airbnb.duplicated(subset = 'listing_id', keep = False)


# In[81]:


# Show all duplicates
airbnb[duplicates].sort_values('listing_id')


# In[82]:


# Get column names from airbnb
column_names = airbnb.columns
column_names


# In[84]:


airbnb['price'] = pd.to_numeric(airbnb['price'].replace('[\$,]', '', regex=True), errors='coerce').fillna(0)


# In[85]:


airbnb


# In[86]:


# Using Aggregate Function on DataFrame
result = airbnb[["price"]].sum()
print(result)


# In[87]:


airbnb['room_type'].unique()


# In[88]:


airbnb['room_type'] = airbnb['room_type'].str.lower().str.strip()

# Replace values in 'room_type' column
airbnb['room_type'] = airbnb['room_type'].replace({
    'private room': 'Private room',
    'entire home/apt': 'Home',
    'private': 'Private room',
    ' shared room': 'Shared room'
})

# Display unique values after replacement
print(airbnb['room_type'].unique())


# In[89]:


airbnb['room_type'] = airbnb['room_type'].str.lower().str.strip()

# Replace values in 'room_type' column
airbnb['room_type'] = airbnb['room_type'].replace({
    'home':'Home'
})

# Display unique values after replacement
print(airbnb['room_type'].unique())


# In[90]:


airbnb.isna().sum()


# In[92]:


# How many values of different room_types do we have?
airbnb['room_type'].value_counts()


# In[93]:


# Remove "(" and ")" from coordinates
airbnb['coordinates'] = airbnb['coordinates'].str.replace("(","")
airbnb['coordinates'] = airbnb['coordinates'].str.replace(")","")
# Print the header of the column
airbnb['coordinates'].head()


# In[94]:


# Split column into two
lat_long = airbnb['coordinates'].str.split(",", expand = True)
lat_long.head()


# In[95]:


# Assign correct columns to latitude and longitude columns in airbnb
airbnb['latitude'] = lat_long[0]
airbnb['longitude'] = lat_long[1]
# Print the header and confirm new column creation
airbnb.head()


# In[96]:


# Print out dtypes again
airbnb.dtypes


# In[97]:


# Convert latitude and longitude to float
airbnb['latitude'] = airbnb['latitude'].astype('float')
airbnb['longitude'] = airbnb['longitude'].astype('float')
# Print dtypes again
airbnb.dtypes


# In[98]:


# Drop coordinates column
airbnb.drop('coordinates', axis = 1, inplace = True)


# In[100]:


# Calculate mean of price without conversion
airbnb['price'].mean()


# In[141]:


# Doing some sanity checks on date data
today = dt.date.today()
today


# In[142]:


# Are there reviews in the future?
airbnb[airbnb['last_review'].dt.date > today]


# In[143]:


# Are there listings in the future?
airbnb[airbnb['listing_added'].dt.date > today]


# In[144]:


#checkimg the right data
airbnb = airbnb[~(airbnb['listing_added'].dt.date > today)]


# In[145]:


# Are there any listings with listing_added > last_review
inconsistent_dates = airbnb[airbnb['listing_added'].dt.date > airbnb['last_review'].dt.date]
inconsistent_dates


# In[104]:


# Print header of two columns
airbnb[['listing_added', 'last_review']].head()


# In[105]:


# Convert both columns to datetime
airbnb['listing_added'] = pd.to_datetime(airbnb['listing_added'], format = '%Y-%m-%d')
airbnb['last_review'] = pd.to_datetime(airbnb['last_review'], format = '%Y-%m-%d')


# In[106]:


# Print header and datatypes of both columns again
print(airbnb[['listing_added', 'last_review']].head())
print(airbnb[['listing_added', 'last_review']].dtypes)


# In[107]:


# Print header of column
airbnb['neighbourhood_full'].head()


# In[108]:


# Split neighbourhood_full
borough_neighbourhood = airbnb['neighbourhood_full'].str.split(",", expand = True)
borough_neighbourhood.head()


# In[109]:


# Create borough and neighbourhood columns
airbnb['borough'] = borough_neighbourhood[0]
airbnb['neighbourhood'] = borough_neighbourhood[1]
# Print header of columns
airbnb[['neighbourhood_full', 'borough', 'neighbourhood']].head()


# In[110]:


# Drop neighbourhood_full column
airbnb.drop('neighbourhood_full', axis = 1, inplace = True)


# In[111]:


# Print out unique values of borough and neighbourhood
print(airbnb['borough'].unique())
print(airbnb['neighbourhood'].unique())


# In[112]:


# Strip white space from neighbourhood column
airbnb['neighbourhood'] =airbnb['neighbourhood'].str.strip()
# Print unique values again
print(airbnb['neighbourhood'].unique())


# In[113]:


# Isolate rows of rating > 5.0
airbnb[airbnb['rating'] > 5.0]


# In[114]:


# Drop these rows and make sure we have effected changes
airbnb.drop(airbnb[airbnb['rating'] > 5.0].index, inplace = True)


# In[115]:


# Get the maximum
airbnb['rating'].max()


# In[116]:


# Understand DataFrame with missing values in rating, number_of_stays, 5_stars, reviews_per_month
airbnb[airbnb['rating'].isna()].describe()


# In[117]:


# Understand DataFrame with missing values in rating, number_of_stays, 5_stars, reviews_per_month
airbnb[~airbnb['rating'].isna()].describe()


# In[118]:


# Impute missing data
airbnb = airbnb.fillna({'reviews_per_month':0,
                        'number_of_stays':0,
                        '5_stars':0})

# Create is_rated column
is_rated = np.where(airbnb['rating'].isna() == True, 0, 1)
airbnb['is_rated'] = is_rated


# In[119]:


airbnb.isna().sum()


# In[120]:


# Investigate DataFrame with missing values in price
airbnb[airbnb['price'].isna()].describe()


# In[121]:


# Investigate DataFrame with missing values in price
airbnb[~airbnb['price'].isna()].describe()


# In[125]:


# Get mean price per room_type
airbnb.groupby('room_type')['price'].mean()


# In[126]:


# Impute price based on conditions
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'Home'), 'price'] = 205.63
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'private room'), 'price'] = 85.51
airbnb.loc[(airbnb['price'].isna()) & (airbnb['room_type'] == 'shared room'), 'price'] = 68.23


# In[127]:


airbnb['price'].dtype


# In[128]:


# Confirm price has been imputed
airbnb.isna().sum()


# In[130]:


result = airbnb[["price"]].sum()
print(result)


# In[131]:


airbnb


# In[139]:


# Are there any listings with listing_added > last_review
inconsistent_dates = airbnb[airbnb['listing_added'].dt.date > airbnb['last_review'].dt.date]
inconsistent_dates


# In[140]:


inconsistent_dates.shape


# In[146]:


airbnb.isna().sum()


# In[150]:


airbnb = airbnb.dropna(subset=['last_review'])


# In[152]:


airbnb


# In[132]:


get_ipython().system('pip install pymongo')


# In[135]:


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Safy:1234@cluster0.4w8kary.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# In[153]:


import pandas as pd
import pymongo

# MongoDB connection parameters
mongodb_uri = "mongodb+srv://Safy:1234@cluster0.4w8kary.mongodb.net/?retryWrites=true&w=majority"
database_name = "AirBnb"  # Replace with your database name
collection_name = "airbnb"  # Replace with your collection name

# Create a MongoClient to connect to your MongoDB Atlas cluster
client = pymongo.MongoClient(mongodb_uri)

# Access the desired database and collection
db = client[database_name]
collection = db[collection_name]

# Convert the DataFrame to a list of dictionaries (one dictionary per row)
data_dict_list = airbnb.to_dict(orient='records')

# Insert the data into MongoDB
collection.insert_many(data_dict_list)

# Close the MongoDB connection
client.close()

print("Data has been successfully inserted into MongoDB Atlas.")


# In[ ]:




