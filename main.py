import requests


params = {
    'nTqmM': '',
    'lang': 'ru'
}
url_template = 'http://www.wttr.in/{}'
cities = ('Лондон', 'Шереметьево', 'Череповец')
for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
