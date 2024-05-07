import os
import shutil
from datetime import datetime
from pathlib import Path
import sys

def backup_files(source_dir, backup_dir):
    source_dir = Path(source_dir)
    backup_dir = Path(backup_dir)

    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    for file in source_dir.iterdir():
        if file.is_file():
            backup_file = backup_dir / f"{timestamp}_{file.name}"
            try:
                shutil.copy(file, backup_file)
                print(f"Файл {file} успешно скопирован как {backup_file}")
            except IOError as e:
                print(f"Не удалось скопировать файл {file}. Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python backup_script.py <исходная_директория> <директория_резервных_копий>")
        sys.exit(1)

    source_dir, backup_dir = sys.argv[1], sys.argv[2]
    backup_files(source_dir, backup_dir)