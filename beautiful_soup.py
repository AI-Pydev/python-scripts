import requests
from bs4 import BeautifulSoup
wiki_url = requests.get('https://en.wikipedia.org/wiki/List_of_territorial_entities_where_English_is_an_official_language').text
soup = BeautifulSoup(wiki_url,'lxml')
tables = soup.find_all('table',{'class':'wikitable sortable'})
country_list = list()
for table in tables:
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all('td')[2].get_text().strip()
        if tds.isalpha() and len(tds) == 3:
            country_list.append(tds)
print(country_list)
