#  Программа управление библиотекой. Применено функциональное программирование

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


def def_shoose_command(dict_command: dict):
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
    

def def_find_command(command: int, book_json: dict):
    # функция определения команды работы 
    if command == 1:
        book_json = def_add_book(book_json)
    elif command == 2:
        book_json = def_delete_book(book_json)        
    elif command == 3:
        def_find_book(book_json)
    elif command == 4:
        def_show_books(book_json, True)
    elif command == 5:
        book_json = def_change_status_book(book_json)        
    return book_json


def def_add_book(book_json: dict):
    # функция добавления книги
    print('\nКоманда добавления книги')
    title = input('Введите наименование \n')
    author = input('Введите автора \n')
    year = def_enter_date()
    
    # определяю ID по последнему значению +1
    quantity_book = len(book_json)
    if quantity_book:
        id_books = list(book_json.keys())
        id = id_books[quantity_book-1] + 1
    else:
        # книг нет 
        id = 1
    # сохраняю книгу
    book_json.update({id:[title, author, year, False]})

    # вывод сохраненной книги
    print('Книга сохранена')

    def_show_books({id:[title, author, year, False]},)

    return book_json


def def_delete_book(book_json: dict):
    # функция удаления книги
    if book_json == {}:
        print('В библиотеке нет книг!')
        return book_json
    print('Удаление книги.')
    while True:
        # проверка на число
        try:
            id = int(input('\nВведите номер id книги которую необходимо удалить\n'
                            'или введите 0, для выхода в главное меню\n'))
            # обработка числа
            if id: # 0 дает False
                book_json.pop(id)
                print('Книга удалена!')
            break

        except (ValueError):
            print('Введите число!')
        except (KeyError):
            print('Такого id нет в библиотеке!')
    return book_json


def def_find_book(book_json: dict):
    # функция поиска книги
    if book_json == {}:
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
        return
    if command == 1:
        text_find = input('Введите наименование книги\n')
    elif command == 2:
        text_find = input('Введите автора книги\n')
    elif command == 3:
        text_find = def_enter_date()

    show_find = {}
    for id, value in book_json.items():
        if value[command-1] == text_find:
            show_find.update({id: [value[0], value[1], value[2], value[3],]})

    if show_find:
        print('\nРезультат поиска:')
        def_show_books(show_find)
    else:
        print('Книги не найдены')
    return


def def_show_books(book_json: dict, all_books: bool = False):
    # функция отображения  книг
    if book_json == {}:
        print('В библиотеке нет книг!')
        return

    if all_books:
        # вывести все книги
        print('Все книги в библиотеке:')

    template = "{0:3}|{1:30}|{2:20}|{3:11}|{4:15}" #указываю ширину столбца
    print (template.format("id", "название", "автор", "год издания", "статус")) # вывожу наименование столбцов
    print('--------------------------------------------------------------------------------')
    for id, value in book_json.items():
        # определяю статус
        if value[3]:
            status = 'выдана'
        else:
            status = 'в наличие'
        # вывод книг ("id", "название", "автор", "год издания", "статус" )
        print (template.format(id, value[0], value[1], value[2], status))
    return


def def_change_status_book(book_json: dict):
    # функция изменения статуса книги
    if book_json == {}:
        print('В библиотеке нет книг!')
        return book_json
    print('Изменение статуса книги.')

    while True:
        # ввод id, проверка на число
        try:
            id = int(input('\nВведите номер id книги статус которой необходимо изменить\n'
                            'или введите 0, для выхода в главное меню\n'))
            # обработка числа
            if id: # 0 - False
                value_book = book_json[id]
                break
            return book_json #выход

        except (ValueError):
            print('Введите число!')
        except (KeyError):
            print('Такого id нет в библиотеке!')
    
    if value_book[3]:
        status = 'выдана'
    else:
        status = 'в наличие'

    print(f'Текущий статус "{status}"')
    while True:
        # вывод списка статуса
        print ('\nВыберите статус:')
        right_command, command = def_shoose_command(STATUS_DEFAULT)
        if right_command:
            break
    # значение ввыбрано
    if command:
        if command == 1:
             book_json[id][3] = False
        else:
             book_json[id][3] = True
        
        print('Изменения внесены!')
        def_show_books({id:[value_book[0], value_book[1], value_book[2], book_json[id][3]]},)
    return book_json


print('\nВас приветствует программа тестового задания \n'
      ' "Разработка системы управления библиотекой".')

# Шаблон книги
# id        int
# title     str
# author    str
# year      int
# status    bool  ( False- в наличие, 
#                   True -выдана)
book_json = {}

# book_json.update({1:['qq', 'author', 1234, False]})
# book_json.update({2:['qq2', 'author2', 1232, True]})

while True:
    # вывод списка команд
    print ('\nСписок команд:')
    right_command, command = def_shoose_command(COMMAND_DEFAULT)
    if right_command:
        if command:
            book_json = def_find_command(command, book_json)
        else:
            break

print('\nПрограмма закончила свою работу')
