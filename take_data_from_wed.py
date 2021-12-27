import re
import datetime

data_dict = {}


def create_pattern (list_word):
    _patt =r""
    for count, word_find in enumerate(list_word):
        if count == len(list_word) - 1:
            _patt += word_find
        else:
            _patt += word_find + "|"

    return _patt


def take_data(beat_soup, pattern_):


    date = beat_soup.find('span', class_="tm-article-snippet__datetime-published")
    date = date.next['title']
    date = datetime.datetime.strptime(date, '%Y-%m-%d, %H:%M')
    title = beat_soup.find('a', class_='tm-article-snippet__title-link').text
    count_view =beat_soup.find('span',class_='tm-icon-counter tm-data-icons__item').text
    # preview = beat_soup.find('div', class_='article-formatted-body article-formatted-body_version-2').text
    try:
        preview = beat_soup.find('div', class_='article-formatted-body article-formatted-body_version-2').text
    except AttributeError:
        preview = beat_soup.find('div', class_='article-formatted-body article-formatted-body_version-1').text

    link = beat_soup.find('a', class_='tm-article-snippet__readmore')
    link = "https://habr.com" + link['href']

    dict_data = {'date': date,
                 'title': title,
                 'link': link,
                 'preview': preview,
                 'count_view': count_view}

    if len(re.findall(pattern_, preview, re.MULTILINE)) > 0 or len(re.findall(pattern_, title, re.MULTILINE)):
        print(f'{date} : {title} {link}\n{preview}\n{count_view} ')
        print("________________")
    return dict_data



