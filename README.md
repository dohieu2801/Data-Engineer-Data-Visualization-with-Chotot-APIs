# Project_thanhthuy
This is project for DE. I crawl data from chotot by API. The, using AWS EC2 with free tier account to transform data.
Finally, insert data to postgre which supply by render. It helps many users can querry data at anywhere.
# Code include:
## 1.Config.yaml:
Information about API, table, columns in table and map table which is supply by user.
## 2.Logging in log:
Write info, error when run code.
## 3.src/utils include: 
Crawler to crawl data
Generate table to parse table which I want
Process to process data: rename columns, remove duplicates, drop na, caculate somethings...
Push data to insert data to postgre.
## 4.src/main:
To run code: /bin/python3 {path}
I set cron job * /30 * * * *
Next, I will get information and visualization to get decision for property.
