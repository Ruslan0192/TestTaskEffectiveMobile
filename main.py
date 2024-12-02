
from command import def_find_command, def_shoose_command, COMMAND_DEFAULT

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
