import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로


dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    info = {}
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80: 
        info['company'] = parsed_data['company']['name']
        info['lat'] = parsed_data['address']['geo']['lat']
        info['lng'] = parsed_data['address']['geo']['lng']
        info['name'] = parsed_data['name']
        dummy_data.append(info)

print(dummy_data)