Конечно! Вот пример программы на языке Python, которая копирует файл из одного каталога в другой с использованием модуля `shutil`:

```python
import shutil
import os

def copy_file(src_file, dest_dir):
    # Проверяем, существует ли исходный файл
    if not os.path.isfile(src_file):
        print(f"Файл {src_file} не существует.")
        return

    # Проверяем, существует ли целевой каталог, если нет, создаем его
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Копируем файл
    try:
        shutil.copy(src_file, dest_dir)
        print(f"Файл {src_file} успешно скопирован в {dest_dir}")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

# Пример использования
src_file = 'путь/к/исходному/файлу.txt'
dest_dir = 'путь/к/целевому/каталогу'

copy_file(src_file, dest_dir)
```

Этот скрипт выполняет следующие шаги:
1. Проверяет, существует ли исходный файл.
2. Проверяет, существует ли целевой каталог, и создает его, если он не существует.
3. Копирует файл в целевой каталог.

Не забудьте заменить `'путь/к/исходному/файлу.txt'` и `'путь/к/целевому/каталогу'` на реальные пути к вашему файлу и каталогу.