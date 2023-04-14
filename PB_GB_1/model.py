phone_book = []
start_phone_book = []
start_phone_book1 = []
res_replace = ''
xxx = []
PATH = 'phone_book.txt'


def get_pb():
    return phone_book


def load_file():
    global phone_book, start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()


def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def search_data(data_cont):
    res_search = []
    all_contacts = open(PATH, 'r', encoding='UTF-8').readlines()
    for contact in all_contacts:
        if data_cont in contact:
            contact = contact.strip().split(';')
            res_search.append({'name': contact[0],
                               'phone': contact[1],
                               'comment': contact[2]})
    return res_search


def change_contact(number_contact, res_text):
    global xxx, start_phone_book, phone_book
    for title, value in res_text.items():
        xxx.append(''.join(value.split()))
    new_contact = ';'.join(xxx) + '\n'
    with open(PATH, 'r', encoding='UTF-8') as c_contacts:
        chang_contact = c_contacts.readlines()
        for x in range(len(chang_contact)):
            if number_contact == x + 1:
                contact = new_contact.strip().split(';')
                phone_book.append({'name': contact[0],
                                   'phone': contact[1],
                                   'comment': contact[2]})


def del_contact(contact):
    global phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        for count, value in enumerate(file, 1):
            if contact == count:
                phone_book.pop(count - 1)


def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
