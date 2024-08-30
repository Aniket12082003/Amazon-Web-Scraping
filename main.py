import re
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import datetime

# Connect to Website and pull in data

URL = 'https://www.amazon.com/Data-Analyst-Programmer-Accountant-T-Shirt/dp/B0C1TCPZG5/ref=sr_1_10?crid=1Y2MM2X34WCZ6&dib=eyJ2IjoiMSJ9.dmE_vrFhOrEPexyMKSLBn69k370RHaKRAALUp3aO07gcEGz6JBeylsNMJjSYmCblSLgP7nr5mX9nIOAphyRfg3QaAUDGBTV9ercl_7ywzbCVsLtwcED_WFDNVbcWYWoUV0rgbMXbQRxAEzxtbnoor5Dlwi_HuXTpY8mTTeE2faLZj0mYPoY--gk_OhezSM-_wadXB5S_3QlEgEl6Z8i36eGNkKA2aJiASkm8vkMIYCgCgUZCqQptUoxt8caQcGt7zYf0GcQCLOgYKdpxmSQfchv4GGk-A_2h6nFpT1DoVRo.KlZlet_1KLVD-UjrposEFbfR2bgVK33io3r9UzZJs1Q&dib_tag=se&keywords=data+analyst+tshirt&qid=1721536701&sprefix=data+analyst+tshirt%2Caps%2C1008&sr=8-10'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

spans = soup2.find_all('span', attrs={'aria-hidden' : 'true'})

price = [span.get_text() for span in spans]

found_price = [m.group(1) 
                for i in price
                    for m in [re.search(r'(\d+[.]\d+)', i)] if m
]

for i in found_price:
    price = i

price = price.strip()[::]
title = title.strip()

print(title)
print(price)

today = datetime.date.today()
print(today)

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

df = pd.read_csv(r'AmazonWebScraperDataset.csv')
print(df)