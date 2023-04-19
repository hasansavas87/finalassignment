#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('mamba install html5lib==1.1 -y')
get_ipython().system('pip install lxml==4.6.4')
#!pip install plotly==5.3.1


# In[ ]:


pip install yfinance


# In[ ]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[ ]:


import yfinance as yf


# In[ ]:


tesla = yf.Ticker('TSLA')


# In[ ]:


tesla_data = tesla.history()
tesla_data.head()


# In[ ]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[ ]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[ ]:


tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[ ]:


GameStop = yf.Ticker("GME")


# In[ ]:


gme_data = GameStop.history(period = 'max')


# In[ ]:


gme_data.reset_index(inplace = True)
gme_data.head()


# In[ ]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[ ]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[ ]:


gme_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[ ]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
gme_revenue.tail()


# In[ ]:


GameStop = yf.Ticker("GME")


# In[ ]:


gme_data = GameStop.history(period = 'max')


# In[ ]:


gme_data.reset_index(inplace = True)
gme_data.head()


# In[ ]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[ ]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[ ]:


gme_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[ ]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
gme_revenue.tail()


# In[ ]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[ ]:


make_graph(gme_data, gme_revenue, 'GameStop')

