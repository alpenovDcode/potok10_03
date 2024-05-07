import os

class Entry:
    def __init__(self, date, author, message):
        self.date = date
        self.author = author
        self.message = message

    def __str__(self):
        return f"Дата: {self.date}\nАвтор: {self.author}\nСообщение: {self.message}\n"


'''
- `__init__`:
  - `filepath`: Путь к файлу, где хранятся записи журнала.
  - `entries`: Список для хранения объектов `Entry`.
  - Метод `load_entries()` вызывается сразу после инициализации 
  объекта для загрузки существующих записей из файла.
  
  - **`load_entries`**:
  - Проверяет существование файла журнала. Если файла нет, метод возвращает `None`.
  - Читает весь файл и разделяет его на блоки по двойным переводам строк (`\n\n`), каждый 
  из которых представляет одну запись.
  - Каждая запись разбивается на части по символу перевода строки (`\n`), и далее каждая 
  строка разбивается по символу `:`, чтобы извлечь значения даты, автора и сообщения, 
  которые затем используются для создания объектов `Entry`.
'''


class Journal:
    def __init__(self, file_path):
        self.entries = []
        self.file_path = file_path

    def add_entries(self, entry):
        self.entries.append(entry)
        self.save_entries()

    def save_entries(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for entry in self.entries:
                f.write(str(entry))


    '''
      - **`load_entries`**:
  - Проверяет существование файла журнала. Если файла нет, метод возвращает `None`.
  - Читает весь файл и разделяет его на блоки по двойным переводам строк (`\n\n`), каждый 
  из которых представляет одну запись.
  - Каждая запись разбивается на части по символу перевода строки (`\n`), и далее каждая 
  строка разбивается по символу `:`, чтобы извлечь значения даты, автора и сообщения, 
  которые затем используются для создания объектов `Entry`.
    '''
    def load_entries(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        entries = content.split("\n\n")
        for entry in entries:
            date, author, message = entry.split('\n')
            author = author.split(': ')[1]
            message = message.split(': ')[1]
            date = date.split(': ')[1]
            self.entries.append(Entry(date, author, message))

    '''
    - **`delete_entry`**:
  - Удаляет запись по указанному индексу из списка `entries`, если индекс валиден.
  - Вызывает `save_entries()` для обновления файла.
    '''
    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self.save_entries()

    '''
    - **`update_entry`**:
  - Обновляет атрибуты выбранной записи, если предоставлены новые значения.
  - Только непустые значения параметров используются для обновления соответствующих 
  атрибутов записи.
  - Вызывает `save_entries()` после внесения изменений.
    '''
    def update_entries(self, index, date=None, author=None, message=None):
        if 0 <= index < len(self.entries):
            if date:
                self.entries[index].date = date
            if author:
                self.entries[index].author = author
            if message:
                self.entries[index].message = message
            self.save_entries()

    '''
    - **`search_entries`**:
  - Ищет и возвращает список записей, содержащих заданное ключевое слово в сообщении. 
  Поиск нечувствителен к регистру.
  '''
    def search_entries(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in entry.message.lower()]

    '''
    - **`__str__`**:
    - Возвращает строковое представление всех записей, 
  объединенных переводом строки. Это удобно для вывода всего журнала одной строкой.
    '''

    def __str__(self):
        return '\n'.join(str(entry) for entry in self.entries)





'''
- **`'r'`** (read): Открытие файла для чтения. Это значение устанавливается по умолчанию, если режим не указан. Если файл не существует, возникает ошибка.
- **`'w'`** (write): Открытие файла для записи. Если файл существует, его содержимое удаляется перед записью. Если файл не существует, создается новый.
- **`'a'`** (append): Открытие файла для дописывания. Если файл существует, данные будут добавлены в конец файла без удаления существующего содержимого. Если файл не существует, создается новый.
- **`'x'`** (exclusive creation): Создание нового файла. Если файл уже существует, возникает ошибка.
- **`'b'`** (binary): Открытие файла в бинарном режиме, например, для работы с файлами изображений или видео.
- **`'t'`** (text): Открытие файла в текстовом режиме (по умолчанию). Подходит для текстовых файлов.
- **`'+'`**: Открытие файла для обновления (чтения и записи), работает в сочетании с другими режимами (например, `'r+'`, `'w+'`, `'a+'`).
'''