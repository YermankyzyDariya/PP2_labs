import psycopg2


conn = psycopg2.connect(
    dbname='postgres',  
    user='postgres',  
    password='12345678',  
    host='localhost',  
    port='5432'  
)
conn.autocommit = True
cursor = conn.cursor()


def search_by_pattern(pattern):
    cursor.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    return cursor.fetchall()


def upsert_user(name, phone):
    cursor.execute("CALL upsert_user(%s, %s);", (name, phone))


def insert_many_users_return_invalid(names, phones):
    cursor.execute("SELECT * FROM insert_many_users_return_invalid(%s, %s);", (names, phones))
    return [row[0] for row in cursor.fetchall()]


def get_paginated(limit, offset):
    cursor.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    return cursor.fetchall()


def delete_user(identifier):
    cursor.execute("CALL delete_user(%s);", (identifier,))


if __name__ == '__main__':
    pattern = input("Введите паттерн для поиска (например, 'Ali'): ")
    results = search_by_pattern(pattern)
    print("Результаты поиска:", results)

    
    name = input("Введите имя пользователя для вставки или обновления: ")
    phone = input("Введите телефон пользователя: ")
    upsert_user(name, phone)
    print(f"Пользователь {name} с телефоном {phone} был вставлен или обновлён.")

   
    names = input("Введите имена пользователей через запятую: ").split(',')
    phones = input("Введите телефоны пользователей через запятую: ").split(',')
    invalid_entries = insert_many_users_return_invalid(names, phones)
    if invalid_entries:
        print("Неверные данные:", invalid_entries)
    else:
        print("Все данные корректны и успешно добавлены.")

    
    limit = int(input("Введите количество записей на страницу: "))
    offset = int(input("Введите смещение (страница): "))
    paginated_results = get_paginated(limit, offset)
    print("Пагинированные результаты:", paginated_results)

    
    identifier = input("Введите имя или телефон для удаления пользователя: ")
    delete_user(identifier)
    print(f"Пользователь с идентификатором {identifier} был удалён.")
