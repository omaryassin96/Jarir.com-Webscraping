import urllib.request as url
from bs4 import BeautifulSoup as bs
from datetime import date

# Opening Today's Scraping File for Storage:

f = open('jarir_laptops_{}.csv'.format(date.today()), 'w')

# Opening Laptops Page & Making a soup out of it:

u = 'https://www.jarir.com/sa-en/computers-peripherals/laptops.html'
req = url.Request(u, headers={'User-Agent' : "Magic Browser"}) 
con = url.urlopen(req)
soup = bs(con.read())

# Extracting each item to a list:
# Jarir.com categorizes the items in its page into 'item last', 'item first', and 'item'.

item_last = soup.findAll('li',{'class':'item last'})
item_first = soup.findAll('li',{'class':'item first'})
item = soup.findAll('li',{'class':'item'})

items = item_last + item_first + item

# Extracting urls from each item:

for item in items:
    laptop_url = item.a['href']
    req = url.Request(laptop_url, headers={'User-Agent' : "Magic Browser"})
    con = url.urlopen(req)
    soup = bs(con.read())
    
    print(laptop_url)
    # Extracting data:
    data = soup.findAll('div',{'id':'card-specifications'})[0]
    rows = data.findAll('tr',{'class':'table__row'})
    for row in rows:
        f.write(row.td.text + ',')
    f.write('\n')
    
    # Closing Today's Scraping File:

f.close()
