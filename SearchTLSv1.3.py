Here is a code snippet to list websites supporting TLSv1.3 and X25519 in Google search and in Netcraft's SSL Server Rating report:
import requests 
from bs4 import BeautifulSoup 

url = 'https://google.com/search?q=site%3A*.com+X25519+TLSv1.3' 
r = requests.get(url) 
soup = BeautifulSoup(r.text, 'html.parser') 
links = soup.find_all('a') 

sites = [] 
for link in links: 
    site = link.get_text() 
    sites.append('https://' + site)  

print('Sites from Google search:') 
print(*sites, sep='\n') 

url = 'https://www.netcraft.com/ssl-server-rating-report.html' 
r = requests.get(url) 
soup = BeautifulSoup(r.text, 'html.parser') 
tables = soup.find_all('table') 

for table in tables: 
    if 'TLS 1.3' in table.text and 'X25519' in table.text: 
        rows = table.find_all('tr') 
        for row in rows: 
            cols = row.find_all('td') 
            link = cols[0].a['href'] 
            site = link.split('/')[2] 
            sites.append('https://' + site)  

print('Sites from Netcraft report:') 
print(*sites, sep='\n')

This will print lists of sites supporting TLSv1.3 and X25519 from:

A Google search query 
Netcraft's SSL Server Rating report 

Let me know if you have any issues running the code.