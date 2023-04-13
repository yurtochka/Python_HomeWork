import text_fields as txt


def main_menu() -> int:
    print('''Главное меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать все контакты
        4. Создать контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход''')
    choice = ''
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(
                choice) < 9:  # ленивый if - если введено не число, то до 2 условия программа не дойдет
            return int(choice)
        else:
            print('Введите число от 1 до 8')


def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def show_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('-' * 63 + '\n')
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def search_contacts():
    print()
    info_contact = input(txt.search_contact)
    return info_contact


def number_change_book():
    line_change = input(txt.num_contact)
    return line_change


def change_text():
    changes_text = input(txt.edit_text)
    return changes_text


def del_contact():
    contact_number = int(input(txt.deleted_cont))
    return contact_number


def confirm(message: str) -> bool:
    answer = input(message + ' (y/n) -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False
