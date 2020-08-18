# Importing relevant libs
import urllib.request as url
from bs4 import BeautifulSoup as bs
from datetime import date


# Opening Today's Scraping File for Storage:
f = open('jarir_laptops_{}.csv'.format(date.today()), 'w')


# Opening Jarir's Laptops Homepage & Making a soup out of it:
# note: I used "req/con" lines instead of the conventional method; beacause I got a (403 Access Forbidden) error when I used the conventional code.
# Here I plugged in jarir's laptops homepage in the variable 'u':
u = 'https://www.jarir.com/sa-en/computers-peripherals/laptops.html'
req = url.Request(u, headers={'User-Agent' : "Magic Browser"}) 
con = url.urlopen(req)
soup = bs(con.read())


# Extracting all laptops' cards in Laptops Homepage:
# note: Jarir.com categorizes the items in its pages into 'item last', 'item first', and 'item'.
item_last = soup.findAll('li',{'class':'item last'})
item_first = soup.findAll('li',{'class':'item first'})
item = soup.findAll('li',{'class':'item'})
items = item_last + item_first + item


# Extracting laptop url from each laptop card:
for item in items:
    laptop_url = item.a['href']
    req = url.Request(laptop_url, headers={'User-Agent' : "Magic Browser"})
    con = url.urlopen(req)
    # Creating a soup out of
    soup = bs(con.read())
    # Printing urls to ensure the code is running and navigating through different pages and urls
    print(laptop_url)
    # Extracting data from internal tables after accessing each laptop's special page:
    data = soup.findAll('div',{'id':'card-specifications'})[0]
    rows = data.findAll('tr',{'class':'table__row'})
    for row in rows:
        f.write(row.td.text + ',')
    f.write('\n')

    
# Closing Today's Scraping file:
f.close()
