import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345678"
)
cur = conn.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(15) NOT NULL
        );
    """)
    conn.commit()


def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data inserted from CSV.")


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Data inserted from console.")


def update_data():
    old_name = input("Enter the name you want to update: ")
    new_name = input("New name (press Enter to skip): ")
    new_phone = input("New phone (press Enter to skip): ")

    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("Data updated.")


def query_data():
    print("Filter by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM PhoneBook")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_data():
    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Your choice: ")

    if choice == '1':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    elif choice == '2':
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted.")


def menu():
    create_table()
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == '1':
            insert_from_csv("/Users/daryaermankyzy/Desktop/Новая папка/L10/phonebook.csv")  # Replace with your file path
        elif option == '2':
            insert_from_console()
        elif option == '3':
            update_data()
        elif option == '4':
            query_data()
        elif option == '5':
            delete_data()
        elif option == '6':
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()
