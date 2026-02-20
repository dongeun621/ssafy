import requests

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(i):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    info = {}
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80: 
        info[parsed_data['company']['name']] = [parsed_data['name']]
        censorship(info)

def censorship(info):
    for i in black_list:
        company = list(info.keys())[0]
        if i == company:
            print(f'{company} 소속의 {info[company][0]} 은/는 등록할 수 없습니다')
            return
    print('이상 없습니다.')

for i in range(1,11):
    create_user(i)