#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
movie_url="https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies"
movie_data = urlopen(movie_url)
movie_html = movie_data.read()
movie_data.close()
print(movie_html)


# In[2]:


from bs4 import BeautifulSoup as soup
movie_soup = soup(movie_html,'html.parser')
print(movie_soup)


# In[4]:


tables=movie_soup.findAll('table',{'class':'wikitable'})
print(tables)


# In[6]:


headers = tables[0].findAll('th',{})
print(headers)


# In[9]:


column_title = [ct.text for ct in headers[:-1]]
print(column_title)


# In[11]:


row_data = tables[0].findAll('tr',{})[1:]
row_details=[]
for row in row_data:
    current_row=[]
    details=row.findAll('td')[:-1]
    for i in details:
        current_row.append(i.text)
    row_details.append(current_row)
print(row_details)


# In[14]:


file_name="top_100_movies.csv"
with open(file_name,'w',encoding='utf-8') as f:
    header_string = ','.join(column_title)
    header_string += '\n'
    f.write(header_string)
    
    for row in row_details:
        row_data = ""
        for w in row:
            w = w.replace(',',' ')
            row_data += w + ','
        row_data +="\n"
        f.write(row_data)
    


# In[15]:


import pandas as pd
file = pd.read_csv('top_100_movies.csv')
file.head(n=10)


# In[ ]:




