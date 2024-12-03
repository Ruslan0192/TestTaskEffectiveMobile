#  Программа управление библиотекой. Применено ООП

COMMAND_DEFAULT = {
    1: 'добавить книгу',
    2: 'удалить книгу',
    3: 'найти книгу',
    4: 'весь список книг',
    5: 'изменить статус книги',
    0: 'выход',
}

PARAMETR_FIND = {
    1: 'по наименованию',
    2: 'по автору',
    3: 'по году издания',
    0: 'главное меню',
}

STATUS_DEFAULT = {
    1: 'в наличии',
    2: 'выдана',
    0: 'главное меню',
}


class Book:
    def __init__(self, title: str, author: str, year: int, status: str):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def def_find_in_class(self, enter_text: list):
        # параметр ввыбран вводим значение
        if enter_text[0] != '':
             if self.title == enter_text[0]:
                 return True
        if enter_text[1] != '':
             if self.author == enter_text[1]:
                 return True             
        if enter_text[2] != 0:
             if self.year == enter_text[2]:
                 return True          
        return False
    

def def_add_book(books: dict):
    # функция добавления книги
    print('\nКоманда добавления книги')
    title = def_enter_str('Введите наименование \n')
    author = def_enter_str('Введите автора \n')
    year = def_enter_date()
    
    # определяю ID по последнему значению +1
    quantity_book = len(books)
    if quantity_book:
        id_books = list(books.keys())
        id = id_books[quantity_book-1] + 1
    else:
        # книг нет 
        id = 1
    # добавляю в список
    books.update({id: Book(title=title,
                           author=author,
                           year=year,
                           status=STATUS_DEFAULT[1]
                           )})

    # вывод сохраненной книги
    print('Книга сохранена')

    def_show_books(books={id: books[id]})

    return books


def def_delete_book(books: dict):
    # функция удаления книги
    if books == {}:
        print('В библиотеке нет книг!')
        return books
    print('Удаление книги.')
    while True:
        # проверка на число
        try:
            id = int(input('\nВведите номер id книги которую необходимо удалить\n'
                            'или введите 0, для выхода в главное меню\n'))
            # обработка числа
            if id: # 0 дает False
                books.pop(id)
                print('Книга удалена!')
            break

        except (ValueError):
            print('Введите число!')
        except (KeyError):
            print('Такого id нет в библиотеке!')
    return books


def def_find_book(books: dict):
    # функция поиска книги
    if books == {}:
        print('В библиотеке нет книг!')
        return

    print('\nПоиск книги.')

    while True:
        # вывод списка параметров
        print ('\nВыберите параметр поиска:')
        right_command, command = def_shoose_command(PARAMETR_FIND)
        if right_command:
            break

    # параметр ввыбран вводим значение
    if command == 0:
        return #команда на выход
    
    enter_text = ['','',0]
    if command == 1:
        enter_text[0] = def_enter_str('Введите наименование книги\n')
    elif command == 2:
        enter_text[1] = def_enter_str('Введите автора книги\n')
    elif command == 3:
        enter_text[2] = def_enter_date()


    show_find = {}
    for id, book in books.items():
        if book.def_find_in_class(enter_text):
            show_find.update({id: book})

    if show_find:
        print('\nРезультат поиска:')
        def_show_books(show_find)
    else:
        print('Книги не найдены')
    return


def def_show_books(books: dict, all_books: bool = False):
    # функция отображения  книг
    if books == {}:
        print('\nВ библиотеке нет книг!')
        return

    if all_books:
        # вывести все книги
        print('\nВсе книги в библиотеке:')

    template = "{0:3}|{1:30}|{2:20}|{3:11}|{4:15}" #указываю ширину столбца
    print (template.format("id", "название", "автор", "год издания", "статус")) # вывожу наименование столбцов
    print('--------------------------------------------------------------------------------')
    for id, book in books.items():
        # вывод книг ("id", "название", "автор", "год издания", "статус" )
        # title, author, year, status = book
        print(template.format(id, book.title, book.author, book.year, book.status))
    return


def def_change_status_book(books: dict):
    # функция изменения статуса книги
    if books == {}:
        print('В библиотеке нет книг!')
        return
    print('Изменение статуса книги.')

    while True:
        # ввод id, проверка на число
        try:
            id = int(input('\nВведите номер id книги статус которой необходимо изменить\n'
                            'или введите 0, для выхода в главное меню\n'))
            # обработка числа
            if id: # 0 - False
                book = books[id]
                break
            return #выход

        except (ValueError):
            print('Введите число!')
        except (KeyError):
            print('Такого id нет в библиотеке!')
    
    print(f'Текущий статус "{book.status}"')
    while True:
        # вывод списка статуса
        print ('\nВыберите статус:')
        right_command, command = def_shoose_command(STATUS_DEFAULT)
        if right_command:
            break

    # значение ввыбрано
    if command:
        book.status = STATUS_DEFAULT[command]
   
        print('Изменения внесены!')
        def_show_books(books={id: book})
    return


def def_enter_str(text: str):
    while True:
        enter_text = input(text)
        if enter_text =='':
            print('Поле не может быть пустым\n')
        else:
            break

    return enter_text


def def_enter_date():
    # ввод и проверка года издания
    while True:
        try:
            year = int(input('Введите год издания, от 1000 до 2024 года" \n'))
            if year < 0:
                print('Введите положительное число!')
            elif 1000 <= year <= 2024:
                break
            else:
                print('Введите число в указанном диапазоне!')
            
        except (ValueError):
            print('Введите число!')
    return year
    

def def_shoose_command(dict_command):
    # функция вывода списка команд и параметров, а также проверки правильного вводо
    for key in dict_command:
        print(f'{key} - {dict_command[key]}')

    # проверка на число
    try:
        # ввод команды
        command = int(input('Введите  соответствующий номер\n'))
        
        # обработка команды
        if 0 <= command <= len(dict_command):
            return True, command
        else:
            print('Такого номера не существует!')
            return False, command

    except (ValueError):
        print('Введите число!')
        return False, 0


def def_find_command(command: int, books: dict):
    # функция определения команды работы 
    if command == 1:
        # добавить книгу
        books = def_add_book(books)
    elif command == 2:
        # удалить книгу
        books = def_delete_book(books)        
    elif command == 3:
        # найти книгу
        def_find_book(books)
    elif command == 4:
        # показать все книги
        def_show_books(books, True)
    elif command == 5:
        # сменить статус
        def_change_status_book(books)        
    return books


books = {} # словарь классов книг, где ключ id
while True:
    # вывод списка команд
    print ('\nСписок команд:')
    right_command, command = def_shoose_command(COMMAND_DEFAULT)
    if right_command:
        if command:
            books = def_find_command(command, books)
        else:
            break

print('\nПрограмма закончила свою работу')