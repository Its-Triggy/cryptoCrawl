# In[1]:
import pandas as pd
from urllib.request import urlopen
import re


# In[2]:


cryptocurrency_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_cryptocurrencies')[0]

print(len(cryptocurrency_df))
cryptocurrency_df.sample(5)


# In[3]:


price_1_df = pd.read_html('https://finance.yahoo.com/cryptocurrencies/?count=100&offset=0')[0]
price_2_df = pd.read_html('https://finance.yahoo.com/cryptocurrencies/?count=100&offset=100')[0]
price_df = price_1_df.append(price_2_df)

price_df.sample(5)


# In[4]:


# Clean up the names of the column headings

for col_name in cryptocurrency_df.columns:
  cryptocurrency_df.rename({col_name : re.sub(r'\([^)]*\)', "", col_name).strip().replace(" ","_")}, axis=1, inplace=True) 

cryptocurrency_df.sample(5)


# In[5]:


#Cleaning up the names of the crypto currencies on price_df
price_df['Name'] = price_df['Name'].apply(lambda x: x.split(" USD")[0].strip())


# In[6]:


joined_on_name_df = cryptocurrency_df.merge(price_df, left_on=["Currency"], right_on =["Name"])

print(len(joined_on_name_df))
joined_on_name_df.sample(5)


# In[8]:


#Clean up the symbols columns and remove citations
cryptocurrency_df=cryptocurrency_df.applymap(lambda x: x.split("[")[0] if type(x) == str else x)
cryptocurrency_df['Symbol'] = cryptocurrency_df['Symbol'].apply(lambda x: x.split(",")[0].strip())

price_df['Symbol'] = price_df['Symbol'].apply(lambda x: x.split("-USD")[0].strip())

#cryptocurrency_df.sample(10)
price_df.sample(10)


# In[9]:


joined_df = cryptocurrency_df.merge(price_df, left_on=["Symbol"], right_on =["Symbol"])

print(len(joined_df))
joined_df.sample(5)


# In[10]:


final_df = joined_df[["Currency", "Symbol", "Price (Intraday)", "Circulating Supply", "Volume in Currency (24Hr)"]]

display(final_df)


# In[ ]:




