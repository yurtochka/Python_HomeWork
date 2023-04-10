# Телефонный справочник


# функция поиска контакта
def search_contact(num_string):
    res_search = []
    all_contacts = open('list_contacts.txt', 'r', encoding='UTF-8').readlines()
    for i in all_contacts:
        if num_string in i:
            res_search.append(i)
    return res_search


# функция изменения контакта
def change_contact(number_contact, edit_t):
    with open('list_contacts.txt', 'r', encoding='UTF-8') as read_list:
        lines = read_list.readlines()
    lines[number_contact - 1] = edit_t + '\n'
    with open('list_contacts.txt', 'w', encoding='UTF-8') as edit_list:
        edit_list.writelines(lines)


# функция удаления контакта
def del_contact(num_str):
    with open('list_contacts.txt', 'r', encoding='UTF-8') as read_list:
        lin = read_list.readlines()
    with open('list_contacts.txt', 'w', encoding='UTF-8') as edit_list:
        del lin[num_str - 1]
        edit_list.write(''.join(lin))



#############################################
def my_menu():
    num_menu = int(input('Меню:'
                         '\n 1. Открыть'
                         '\n 2. Сохранить'
                         '\n 3. Просмотреть контакты'
                         '\n 4. Создать контакт'
                         '\n 5. Найти контакт'
                         '\n 6. Изменить контакт'
                         '\n 7. Удалить контакт'
                         '\n 8. Сортировка списка контактов по алфавиту'
                         '\n 9. Выход'
                         '\n'
                         '\n Введите необходимый пункт меню: '))
    return num_menu


###################################

while True:
    point_menu = my_menu()
    if point_menu == 1:  # открыть файл
        look_file = open('list_contacts.txt', 'r', encoding='UTF-8')
    elif point_menu == 2:  # сохранить файл
        xxx = open('list_contacts.txt', 'r', encoding='UTF-8')
        xxx.close()
        print('Контакты сохранены.')
    elif point_menu == 3:  # просмотреть контакты
        look_file = open('list_contacts.txt', 'r', encoding='UTF-8')
        print()
        print(*look_file)
        print()
        look_file.close()
    elif point_menu == 4:  # создать контакт
        add_contact = open('list_contacts.txt', 'a', encoding='UTF-8')
        print()
        my_text = input('Введите новый контакт, через ";" : ')
        add_contact.write('\n' + my_text + '\n')
        add_contact.close()
        print()
        print('Супер, контакт добавлен в справочник!')
    elif point_menu == 5:  # найти контакт
        print()
        search_text = input('Введите текст для поиска: ')
        my_line = search_contact(search_text)
        print()
        print('Результат поиска:')
        print(*my_line)
        print()
    elif point_menu == 6:  # изменить контакт
        print()
        look_contacts = open('list_contacts.txt', 'r+', encoding='UTF-8')
        for i, item in enumerate(look_contacts, 1):
            print(f'{i}. {item}')
        num_contact = int(input('Введите номер контакта, который хотите изменить: '))
        edit_text = input('На какой текст изменить: ')
        change_contact(num_contact, edit_text)
        print('Справочник благополучно изменен.')
    elif point_menu == 7:  # удалить контакт
        print()
        look_contacts = open('list_contacts.txt', 'r+', encoding='UTF-8')
        for i, item in enumerate(look_contacts, 1):
            print(f'{i}. {item}')
        num_contact = int(input('Введите номер контакта, который хотите удалить: '))
        del_contact(num_contact)
        print('Контакт удален')
        look_contacts.close()
    elif point_menu == 8:  # сортировка справочника
        infile = open('list_contacts.txt', 'r+', encoding='UTF-8')
        infile.writelines('\n')
        lines = []
        for t in infile:
            lines.append(t)
        print(lines)
        lines.sort()
        infile.seek(0)
        infile.writelines(lines)
        infile.close()
        print()
        print('Список контактов отсортирован.')
        print()
    elif point_menu == 9:  # выход из справочника
        break
