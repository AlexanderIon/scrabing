import requests
import bs4

import datetime
from take_data_from_wed import take_data, create_pattern

head ={'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          'Accept-Encoding': "gzip, deflate, br",
          'Accept-Language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          'Cache-Control': 'max-age=0',
          'Connection': 'keep-alive',
          'Cookie': '_ym_d=1632388400; _ym_uid=1632388400979955121; _ga=GA1.2.223737397.1632388401; hl=ru; fl=ru; __gads=ID=4eef55ed80d5f6bd:T=1632388401:S=ALNI_MZRIirdgI3qHQL1Nw-BFXYaOVRhkA; feature_streaming_comments=true; _gid=GA1.2.1395906809.1640268339; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=597669:540500:193284:584806:217291:463933:323310:346362:494720; _gat=1',
          'Host': 'habr.com',
          'If-None-Match': 'W/"39fda-m/WzpbWROsBqBCHGUl83b9Mhjuo"',
          'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
          'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': "Windows",
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

response = requests.get("https://habr.com/ru/all/", headers=head)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.findAll('article')
article = soup.find('article')

KEYWORDS = ['Data', 'работа']
pattern = create_pattern(KEYWORDS)

# date = article.find('span', class_="tm-article-snippet__datetime-published")
# date = datetime.datetime.strptime(date.next['title'], '%Y-%m-%d, %H:%M')
# title = article.find('a',class_='tm-article-snippet__title-link').text
# preview = article.find('div', class_='article-formatted-body article-formatted-body_version-2').text
# link = article.find('a',class_='tm-article-snippet__readmore')
# link = "https://habr.com/ru/all/"+link['href']
# print(date,title,'\n\n', preview,link)

list_articles =[]
for i in range(len(articles)):

    list_articles.append(take_data(articles[i], pattern))


