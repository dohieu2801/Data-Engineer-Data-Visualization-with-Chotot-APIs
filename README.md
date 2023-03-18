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

Firstly, I have some metric: price property, number shop which live at page...

![image](https://user-images.githubusercontent.com/92812173/226100930-add04781-c415-4661-ac80-ed248540c6c1.png)

Secondly, Overall table which use for check price property in cities, distrit, ward. Addtionally, we have information: price average, nuber of property by category...

![image](https://user-images.githubusercontent.com/92812173/226101075-440576e2-3852-43a7-a888-d5ee323a780f.png)

Thirdly, Seller tab provided information about: number,price of property which was supply by shop This help we have a good choice.

![image](https://user-images.githubusercontent.com/92812173/226101240-68683d47-0bb8-4fc4-a9b0-abffa50aba64.png)

Finally, we have price map tab which user can search property by map. You can make a visual comparison based on this tab

![image](https://user-images.githubusercontent.com/92812173/226101334-a6506c69-daf1-42a8-adad-7ef77c0cf4c1.png)

Above are a few tools to help users make basic judgments and choose real estate products that match their criteria.

This is link for pbix file: https://drive.google.com/file/d/1dTkTLPyh1C2VtwipVGUKH4Ktw-Qvaa84/view?usp=share_link




