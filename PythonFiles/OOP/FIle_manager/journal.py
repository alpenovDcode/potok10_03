import os
class Entry:
    def __init__(self, date, author, message):
        self.date = date
        self.author = author
        self.message = message


    def __str__(self):
        return f"Дата: {self.date}\nАвтор: {self.author}\nСообщение: {self.message}\n"


class Journal:
    def __init__(self, file_path):
        self.entries = [] # [date,author,message,date,author,message]
        self.file_path = file_path
        self.load_entries()

    '''
    - **`load_entries`**:
  - Проверяет существование файла журнала. Если файла нет, метод возвращает `None`.
  - Читает весь файл и разделяет его на блоки по двойным переводам строк (`\n\n`), 
  каждый из которых представляет одну запись.
  - Каждая запись разбивается на части по символу перевода строки (`\n`), 
  и далее каждая строка разбивается по символу `:`, чтобы извлечь значения даты, 
  автора и сообщения, которые затем используются для создания объектов `Entry`.
    '''
    def load_entries(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        entries = content.strip().split("\n\n")
        for entry in entries:
            date, author, message = entry.split('\n')
            date = date.split(': ')[1]
            author = author.split(': ')[1]
            message = message.split(': ')[1]
            self.entries.append(Entry(date, author, message))


    def add_entry(self, entry):
        self.entries.append(entry)
        self.save_entries()

    '''
    - **`save_entries`**:
    - Открывает файл журнала в режиме записи (`'w'`), 
    что означает, что содержимое файла будет перезаписано.
    - Записывает каждую запись в файл, используя их строковое представление.'''
    def save_entries(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for i in self.entries:
                file.write(str(i))

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self.save_entries()

    def update_entry(self, index, date=None, author=None, message=None):
        if 0 <= index < len(self.entries):
            if date:
                self.entries[index].date = date
            if author:
                self.entries[index].author = author
            if message:
                self.entries[index].message = message
            self.save_entries()

    def search_entries(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in entry.message.lower()]

    def __str__(self):
        return "\n".join(str(entry) for entry in self.entries)