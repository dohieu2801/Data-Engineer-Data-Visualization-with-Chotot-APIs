!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
#!pip install plotly==5.3.1
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Create make_graph function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1,           col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2,         col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object  
Tesla=yf.Ticker("TSLA")
# Using the ticker object and the function history extract stock information and save it in a dataframe named tesla_data. Set the period parameter to max so we get information for the maximum amount of time.
tesla_data=Tesla.history(period="max")
# reset index
tesla_data.reset_index(inplace=True)
# display first five rows using head() method
tesla_data.head()
# dowload web page with request library
url=" https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data=requests.get(url).text
# parser hte html data with BeautifulSoup
soup=BeautifulSoup(html_data,"html.parser")
# read hmtl 
tesla_revenue = pd.read_html(str(soup))
tesla_revenue=pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    revenue =col[1].text
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue},ignore_index=True)
print(tesla_revenue)
# Clean data_revenue
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue
# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object  
GameStop=yf.Ticker("GME")
# Using the ticker object and the function history extract stock information and save it in a dataframe named tesla_data. Set the period parameter to max so we get information for the maximum amount of 
gme_data=GameStop.history(period="max")
# reset index
gme_data.reset_index(inplace=True)
# display first five rows using head() method
gme_data.head()
# display the last 5 row of the tesla_revenue dataframe using the tail function
tesla_revenue.iloc[8:13]
# dowload web page with request libraryv
url="https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data=requests.get(url).text
# parser hte html data with BeautifulSoup
soup=BeautifulSoup(html_data,"html.parser")
# read hmtl 
gme_revenue = pd.read_html(str(soup))
gme_revenue=pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    revenue =col[1].text
    gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue},ignore_index=True)
print(gme_revenue)
# Clean data_revenue
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
# display the last 5 row of the gme_revenue dataframe using the tail function
gme_revenue.loc[12:17]
# plot of Telsa with make_graph function
make_graph1(tesla_data,tesla_revenue,'Plot of Telsa')
# plot of GME with make_graph function
make_graph1(gme_data,gme_revenue,'Plot of GameStop')
