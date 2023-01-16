import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

URL = "https://theconquerors.fandom.com/wiki/Category:Maps"


#URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL, headers=headers)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

test = soup.findall("table", div="article-table")
no = soup.findAll('table', div_="article-table")[0].findAll('tr')
map_info_dict = {}


for i in range(len(no)):
    c = no[i].find_all("th")
    map_info_dict[c[0].text] = []
    for z in range(len(c)):
        map_info_dict[c[0].text].append(c[z].text)
        #print(c[z].text)



print(map_info_dict)









#print(mydivs.text)