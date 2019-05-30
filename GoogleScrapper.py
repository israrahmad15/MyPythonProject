import requests
import bs4
import re
from bs4 import BeautifulSoup
#search_item = "excel"

base = "http://www.google.de"
url = "https://www.google.co.in/search?source=hp&ei=kyTtXNqKJa3hz7sP7JujuAY&q=awesome+world&oq=awesome+world&gs_l"
#url ="https://mycodingzone.net/blog/english"
data = requests.get(url)
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "lxml")
soup = bs4.BeautifulSoup(data.text, 'html.parser')

#reg=re.compile(".*&sa=")
links1 = []
for item in soup.find_all('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}):
    title = item.decode_contents()

    print(title)

for links in soup.find_all('a'):
    link = links.get('href')
    if link[0:7] == "/url?q=" and link != 'youtube':
        urlf = (link[7:len(link)])
        print(urlf)
		print("Israr")

for para in soup.find_all('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}):
    desc = para.text
    print(desc)
'''
for next_page in soup.select(".fl"):
    res = requests.get(base + next_page.get('href'))
    soup = BeautifulSoup(res.text, "lxml")
    for item in soup.select(".r a"):
 
        print(item.text)
'''