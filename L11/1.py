import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname='phonebook11',
    user='postgres',
    password='12345678',
    host='localhost',
)
cur = conn.cursor()

# 1. Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone TEXT
);
""")

# 2. Функция поиска по шаблону
cur.execute("""
DROP FUNCTION IF EXISTS search_phonebook(TEXT);
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name::TEXT, pb.phone::TEXT
    FROM phonebook pb
    WHERE pb.name ILIKE '%' || pattern || '%'
       OR pb.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# 3. Процедура вставки/обновления одного пользователя
cur.execute("""
DROP PROCEDURE IF EXISTS upsert_user(TEXT, TEXT);
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
""")

# 4. Процедура массовой вставки
cur.execute("""
DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[]);
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            CALL upsert_user(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Incorrect phone: %, name: %', phones[i], names[i];
        END IF;
    END LOOP;
END;
$$;
""")

# 5. Функция пагинации
cur.execute("""
DROP FUNCTION IF EXISTS get_phonebook_paginated(INT, INT);
CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name::TEXT, pb.phone::TEXT
    FROM phonebook pb
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
""")

# 6. Процедура удаления
cur.execute("""
DROP PROCEDURE IF EXISTS delete_user(TEXT);
CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = identifier OR phone = identifier;
END;
$$;
""")

conn.commit()

# Функции для выполнения запросов

def search_by_pattern(pattern):
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    for row in cur.fetchall():
        print("🔎 Found:", row)

def upsert(name, phone):
    cur.execute("CALL upsert_user(%s, %s);", (name, phone))
    conn.commit()

def insert_batch(names, phones):
    cur.execute("CALL insert_many_users(%s, %s);", (names, phones))
    conn.commit()

def paginate(limit, offset):
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    for row in cur.fetchall():
        print("📄 Row:", row)

def delete(identifier):
    cur.execute("CALL delete_user(%s);", (identifier,))
    conn.commit()

# Интерактивное меню
while True:
    print("\nВыберите действие:")
    print("1. Поиск по шаблону")
    print("2. Вставить/обновить одного пользователя")
    print("3. Вставить много пользователей")
    print("4. Пагинация данных")
    print("5. Удалить пользователя")
    print("6. Выйти")
    
    choice = input("Введите номер действия: ")

    if choice == "1":
        pattern = input("Введите шаблон для поиска: ")
        search_by_pattern(pattern)

    elif choice == "2":
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        upsert(name, phone)

    elif choice == "3":
        names_input = input("Введите имена через запятую: ")
        phones_input = input("Введите телефоны через запятую: ")
        names = names_input.split(",")
        phones = phones_input.split(",")
        insert_batch(names, phones)

    elif choice == "4":
        limit = int(input("Введите лимит: "))
        offset = int(input("Введите смещение: "))
        paginate(limit, offset)

    elif choice == "5":
        identifier = input("Введите имя или телефон для удаления: ")
        delete(identifier)

    elif choice == "6":
        print("Выход...")
        break

    else:
        print("Неверный выбор! Попробуйте снова.")

# Закрываем соединение
cur.close()
conn.close()


