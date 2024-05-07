from journal import Journal, Entry

def main_menu():
    journal = Journal("journal.txt")
    print(journal)
    # while True:
    #     print("\nВыберите действие:")
    #     print("1. Добавить запись")
    #     print("2. Показать все записи")
    #     print("3. Удалить запись")
    #     print("4. Обновить запись")
    #     print("5. Поиск по сообщению")
    #     print("6. Выход")
    #
    #     choice = input("Введите номер действия: ")
    #     if choice == '1':
    #         date = input("Введите дату: ")
    #         author = input("Введите автора: ")
    #         message = input("Введите сообщение: ")
    #         journal.add_entries(Entry(date, author, message))
    #     elif choice == '2':
    #         print(journal)
    #     elif choice == '3':
    #         index = int(input("Введите индекс записи для удаления: "))
    #         journal.delete_entry(index)
    #     elif choice == '4':
    #         index = int(input("Введите индекс записи для обновления: "))
    #         date = input("Введите новую дату (оставьте пустым, если не изменять): ")
    #         author = input("Введите нового автора (оставьте пустым, если не изменять): ")
    #         message = input("Введите новое сообщение (оставьте пустым, если не изменять): ")
    #         journal.update_entry(index, date, author, message)
    #     elif choice == '5':
    #         keyword = input("Введите ключевое слово для поиска: ")
    #         results = journal.search_entries(keyword)
    #         for entry in results:
    #             print(entry)
    #     elif choice == '6':
    #         break
    #     else:
    #         print("Неправильный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == '__main__':
    main_menu()
