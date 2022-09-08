import requests
try:
    city_number = int(input('Введите цифру, соответствующую городу, в котором хотите узнать прогноз погоды:'
                        '1 - Лондон, 2 - Шереметьево, 3 - Череповец\n'))
except ValueError:
    print('Ввод не похож на цифру 1, 2, или 3 :)')
    exit(-1)
if city_number not in (1, 2, 3):
    raise ValueError('Введена не корректная цифра')
cities = {1: 'Лондон', 2: 'Шереметьево', 3: 'Череповец'}
url_template = 'https://wttr.in/{}?nTqmM&lang=ru%20HTTP/1.1'
url = url_template.format(cities[city_number])
response = requests.get(url)
response.raise_for_status()
print(response.text)
