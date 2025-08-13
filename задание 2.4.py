
#телефонный справочник

def show_menu():
    print("\nТелефонный справочник:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Найти номер по имени")
    print("4. Удалить запись")
    print("5. Выйти")

def show_all(phonebook):
    if not phonebook:
        print("Справочник пуст.")
    else:
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def add_entry(phonebook):
    name = input("Введите имя: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = number
    print(f"Запись для {name} добавлена.")

def find_number(phonebook):
    name = input("Введите имя для поиска: ")
    number = phonebook.get(name)
    if number:
        print(f"{name}: {number}")
    else:
        print(f"Запись для {name} не найдена.")

def delete_entry(phonebook):
    name = input("Введите имя для удаления: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Запись для {name} удалена.")
    else:
        print(f"Запись для {name} не найдена.")

def main():
    phonebook = {}

    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-5): ")

        if choice == '1':
            show_all(phonebook)
        elif choice == '2':
            add_entry(phonebook)
        elif choice == '3':
            find_number(phonebook)
        elif choice == '4':
            delete_entry(phonebook)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    if name == "__main__":
        main()