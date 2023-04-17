no_contact_or_file = 'Телефонная книга пуста или не открыта'

load_successful = 'Телефонная книга удачно загружена!'
save_successful = 'Телефонная книга успешно сохранена.'

new_contact_successful = 'Контакт успешно создан!'

new_name = 'Введите имя и фамилию контакта: '
new_phone = 'Введите телефон контакта: '
new_comment = 'Введите комментарий контакта: '

search_contact = 'Введите данные по искомому контакту: '
res_search = 'Результат поиска: '
def not_found(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

num_contact = 'Введите номер контакта, который хотите изменить: '
edit_text = 'На какой текст изменить: '
enter_or_empty = 'Введите новый контакт или оставьте пустым'

def successful_edit(name: str) -> str:
    return f'Контакт {name} успешно изменен!'

deleted_cont = 'Введите номер контакта для удаления: '
def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить контакт {name}?'
def delete_contact(name: str) -> str:
    return f'Контакт {name} успешно удален!'

is_changed = 'Были внесены изменения. Сохранить?'

bye_bye = 'Пока Пока'
