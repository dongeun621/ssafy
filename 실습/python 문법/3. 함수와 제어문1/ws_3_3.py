def rental_book(name, books):
    decrease_book(books)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{name}님이 {books}권의 책을 대여하였습니다.')
    pass

number_of_book = 100

def decrease_book(books):
    global number_of_book
    number_of_book -= books
    pass

rental_book('홍길동', 3)