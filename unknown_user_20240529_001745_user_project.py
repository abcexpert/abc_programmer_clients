Конечно! Вот пример программы на Python, которая копирует файл из одного каталога в другой. Для выполнения этой задачи мы будем использовать модуль `shutil`, который предоставляет функции для работы с файлами и каталогами.

```python
import shutil
import os

def copy_file(source_path, destination_path):
    try:
        # Проверяем, существует ли исходный файл
        if not os.path.isfile(source_path):
            print(f"Файл {source_path} не существует.")
            return

        # Создаем каталог назначения, если он не существует
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        # Копируем файл
        shutil.copy2(source_path, destination_path)
        print(f"Файл успешно скопирован из {source_path} в {destination_path}")

    except Exception as e:
        print(f"Произошла ошибка при копировании файла: {e}")

# Пример использования
source = '/path/to/source/file.txt'  # Замените на путь к исходному файлу
destination = '/path/to/destination/file.txt'  # Замените на путь к файлу назначения

copy_file(source, destination)
```

В этом примере:
1. `source_path` — это путь к исходному файлу, который вы хотите скопировать.
2. `destination_path` — это путь к файлу назначения, куда вы хотите скопировать исходный файл.
3. Функция `os.makedirs` создаёт все промежуточные каталоги, если они не существуют.
4. Функция `shutil.copy2` копирует файл и сохраняет метаданные (например, время последней модификации).

Не забудьте заменить `'/path/to/source/file.txt'` и `'/path/to/destination/file.txt'` на реальные пути к вашим файлам.