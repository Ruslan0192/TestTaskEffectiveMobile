Задание: Разработка системы управления библиотекой

Описание

Необходимо разработать консольное приложение для управления библиотекой книг. Приложение должно позволять добавлять, удалять, искать и отображать книги. Каждая книга должна содержать следующие поля:

 • id (уникальный идентификатор, генерируется автоматически)
 
 • title (название книги)
 
 • author (автор книги)
 
 • year (год издания)
 
 • status (статус книги: “в наличии”, “выдана”)
 

Требования
 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
    
 3. Удаление книги: Пользователь вводит idкниги, которую нужно удалить.
    
 5. Поиск книги: Пользователь может искать книги по title, author или year.
    
 7. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
    
 9. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
     

Дополнительные требования

 • Реализовать хранение данных в текстовом или json формате.
 
 • Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
 
 • Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
 
 • Не использовать сторонние библиотеки.


Реализация:

Приложение написано двумя методами:

- функциональное программирование (файл «main.py»);
  
- объектно-ориентированное программирование (файл «main_class.py» и файл «main_class_id.py» )
  
Основное отличие в методе ООП книги определяются классом (классы хранятся в словаре {id: класс}, id не внесен в класс для ускорения работы в файле «main_class.py» в файле файл «main_class_id.py» хранение книг в списке [books] ) в другом случае хранятся в формате json {id: [title, author, year, status}. В обоих вариантах все требования выполнены.

Тестирование произведено автоматически с использованием библиотеки pytest.


Описание работы с классом без id (для других случаев алгоритм аналогичен):

	При старте приложение приветствует пользователя и выводит главное меню:
 
Список команд:

1 - добавить книгу

2 - удалить книгу

3 - найти книгу

4 - весь список книг

5 - изменить статус книги

0 - выход

Введите соответствующий номер


Для удобства пользователей выбор необходимого пункта осуществляется вводом соответствующего номера. За корректный ввод числа отвечает унифицированная функция def_shoose_command(dict_command) -> right_command: bool, command: int (right_command - обрабатывать или нет, command – номер команды) (также она используется для выбора параметра поиска и состояния статуса), функция проверяет на ввод численного значения и его диапазон в пределах заданного словаря {номер пункта: выводимый текст для пользователя}. При значении «0» происходит выход из приложения.

После выбора пункта в функции def_find_command(command: int, books: dict) -> books происходит определение перехода.


п1. 'добавить книгу' (функция def_add_book(books: dict) -> books): 

•	просит ввести пользователя наименование, автора (с проверкой пустой строки функцией def_enter_str(text: str)-> enter_text: str, где text - вопрос) и год издания (с проверкой на число и диапазона дат функцией def_enter_date()-> enter_text :int);

•	инициализирует class Book;

•	определяет текущий id и записывает book c новым ключом id;

•	вывод новой книги унифицированной функцией def_show_books(books: dict, all_books: bool = False)-> None (подробнее о ней в п4)


п2. 'удалить книгу' (функция def_delete_book(books: dict) -> books): 

•	проверка на наличие книг;

•	ввод id с проверкой на число и наличие его в словаре books ;

•	удаление из словаря books.


п3. 'найти книгу' (функция def_find_book(books: dict) -> None): 

•	проверка на наличие книг;

•	выбор параметра поиска;


Поиск книги.

Выберите параметр поиска:

1 - по наименованию

2 - по автору

3 - по году издания

0 - главное меню

Введите соответствующий номер


•	запрос соответствующих данных с вышеуказанными проверками;

•	поиск в функции класса def_find_in_class(self, enter_text: list)->bool (возврат флага наличия записи) 

•	вывод новой книги унифицированной функцией def_show_books(books: dict, all_books: bool = False)-> None (подробнее о ней в п4)


п4. 'весь список книг' (функция def_show_books(books: dict, all_books: bool = False) -> None (аргумент all_books – выводить все книги (True) или для использования другими функциями) : 

•	проверка на наличие книг;

•	вывод форматированной таблицы


п5. 'изменить статус книги' (функция def_show_books(books: dict, all_books: bool = False) -> None (аргумент all_books – выводить все книги (True) или для использования другими функциями) : 

•	проверка на наличие книг;

•	ввод id с проверкой на число и наличие его в словаре books ;

•	вывод текущего статуса и запрос вариантов на изменение;


Выберите статус:

1 - в наличии

2 - выдана

0 - главное меню


•	замена статуса книги

•	вывод книги унифицированной функцией def_show_books(books: dict, all_books: bool = False)-> None (подробнее о ней в п4)
