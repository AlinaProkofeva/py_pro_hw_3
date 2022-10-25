import requests
import bs4

KEYWORDS = ['Save', 'айтишников', 'телефон']

URL = 'https://habr.com/ru/all/'
BASE_URL = 'https://habr.com'

response = requests.get(URL)

soup = bs4.BeautifulSoup(response.text, features='html5lib')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    try: # обрабатываем ошибки, когда страница без тега 'p' или не имеет атрибут текста
        link = f"{BASE_URL}{article.find('h2').find('a').get('href')}" # ссылка на полную статью
        response_article = requests.get(link)
        soup_article = bs4.BeautifulSoup(response_article.text, features='html5lib')
        preview = soup_article.find('article').find('p').text
        preview_words = preview.split(' ')

        for word in preview_words:     # тут логика проверки вхождения в констант-список
            if word in KEYWORDS:
                title = soup_article.find('h1').find('span').text
                date = soup_article.find('time').get('title')[0:10]
                print(f'{date} - {title} - {link}')
    except AttributeError:
        continue

    '''В некоторых статьях в превью идет 1 абзац, в некоторых больше, логику, как это обработать в каждой отдельно
     взятой статье, я не реализовала - не смогла уловить логику самого сайта, по какому признаку определяет, сколько
      абзацев забирать в превью (наверняка по количеству букв, но сколько конкретно, не знаю). Некоторые статьи имеют 
      иное строение и иные теги (редко, но парочка попалась), стандартная логика, подходящая ~95% статей, под них
       не подходит. Здесь в коде я их не обрабатывала, просто закинула в исключения. Тег из примера в домашке не нашла 
       в коде страницы - видимо, поменялась структура сайта. Превью с основной страницы не нашла, как забрать, 
       что бы ни пробовала - возвращается None'''







