'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

def show_menu() -> int:
    print("Выберите действие:\n"
          "1. Отобразить весь список\n"
          "2. Найти по фамилии или имени\n"
          "3. Найти по номеру телефона\n"
          "4. Добавить нового пользователя\n"
          "5. Сохранить справочник в формате csv\n"
          "6. Удалить запись\n"
          "7. Изменить запись\n"
          "8. Закончить работу")
    choice = int(input(">>: "))
    return choice

def read_txt(path):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def close_phone_book(path):
    path.close()

def print_all_book(path):
    for element in path:
        for key in element:
            print(f'{key} : {element[key]}')
        print()

def get_search_name():
    return str(input("Введите Фамилию или Имя для поиска: "))

def find_by_name(path, name):
    result = []
    for elem in path:
        if elem['Фамилия'] == name or elem['Имя'] == name:
            result.append(elem)
    return result

def get_search_number():
    return str(input("Введите телефон для поиска: "))

def find_by_number(path, number):
    result = []
    for elem in path:
        if elem['Телефон'] == number:
            result.append(elem)
    return result

def get_new_user():
    new_record = dict()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for field in fields:
        new_record[field] = input(f"Введите {field}: ")
    return new_record

def add_user(phone_book, user_data):
    phone_book.append(user_data)

def write_txt(filename, data):
    with open(filename, 'w', encoding='utf-8') as file_out:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            file_out.write(f'{s[:-1]}\n')

def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as file_out:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            file_out.write(f'{s[:-1]}\n')
def get_file_name():
    new_file = str(input("Название файла: "))
    new_file += '.csv'
    return new_file

def delete_record(path, name):
    for elem in path:
        if elem['Фамилия'] == name or elem['Имя'] == name:
            index = path.index(elem)
            path.pop(index)

def delete_record_number(path, number):
    for elem in path:
        if elem['Телефон'] == number:
            index = path.index(elem)
            path.pop(index)

def change_record(path, name):
    for elem in path:
        if elem['Фамилия'] == name or elem['Имя'] == name:
            print(f"Фамилия = {elem['Фамилия']}")
            elem['Фамилия'] = str(input("Новая Фамилия: "))
            print(f"Имя = {elem['Имя']}")
            elem['Имя'] = str(input("Новое Имя: "))
            print(f"Телефон = {elem['Телефон']}")
            elem['Телефон'] = str(input("Новый Телефон: "))
            print(f"Описание = {elem['Описание']}")
            elem['Описание'] = str(input("Новое Описание: "))

def change_record_number(path, number):
    for elem in path:
        if elem['Телефон'] == number:
            print(f"Фамилия = {elem['Фамилия']}")
            elem['Фамилия'] = str(input("Новая Фамилия: "))
            print(f"Имя = {elem['Имя']}")
            elem['Имя'] = str(input("Новое Имя: "))
            print(f"Телефон = {elem['Телефон']}")
            elem['Телефон'] = str(input("Новый Телефон: "))
            print(f"Описание = {elem['Описание']}")
            elem['Описание'] = str(input("Новое Описание: "))

print("Программа представляет из себя макет телефонного справочника.")
choice = show_menu()
phone_book = read_txt('phone.txt')

while (choice != 8):
    if choice == 1:
        print_all_book(phone_book)
    elif choice == 2:
        name = get_search_name()
        print_all_book(find_by_name(phone_book, name))
    elif choice == 3:
        number = get_search_number()
        print_all_book(find_by_number(phone_book, number))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_txt('phone.txt', phone_book)
    elif choice == 5:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    elif choice == 6:
        print("Выбрано удаление записи!")
        print("1. Удалить запись по Фамилии или Имени\n"
              "2. Удалить запись по номеру телефона\n"
              "3. Передумал. Отмена.")
        choice_del = int(input('>>: '))
        while (choice_del != 3):
            if choice_del == 1:
                name_delete = get_search_name()
                delete_record(phone_book, name_delete)
                break
            elif choice_del == 2:
                number_delete = get_search_number()
                delete_record_number(phone_book, number_delete)
                break
    elif choice == 7:
        print("Найти запись для изменения:\n"
              "1. По Фамилии или Имени\n"
              "2. По Телефону\n"
              "3. Я передумал.")
        choice_change = int(input('>>: '))
        while (choice_change != 3):
            if choice_change == 1:
                name_change = get_search_name()
                change_record(phone_book, name_change)
                break
            elif choice_change == 2:
                number_change = get_search_number()
                change_record_number(phone_book, number_change)
                break
    choice = show_menu()

    write_txt('phone.txt', phone_book)