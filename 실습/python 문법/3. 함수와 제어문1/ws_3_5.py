number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age):
    user_info = {'name': name, 'age': age}
    print(f'{name}님 환영합니다!')
    return user_info

many_user = list(map(create_user, name, age))
user_info = []
for i in many_user:
    user = {}
    user[i['name']] = i['age']
    user_info.append(user)


def rental_book(info):
    name = list(info.keys())[0]
    age = info[name]
    books = age // 10
    decrease_book(books)
    print(f'{name}님이 {books}권의 책을 대여하였습니다.')
    pass

def decrease_book(books):
    global number_of_book
    number_of_book -= books
    print(f'남은 책의 수 : {number_of_book}')
    pass

for i in user_info:
    rental_book(i)