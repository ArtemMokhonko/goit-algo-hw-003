from pathlib import Path
import shutil

def copy_files_recursively(src_dir: Path, dst_dir: Path):
    """Рекурсивно копіює файли з вихідної директорії до директорії призначення."""
    # Перебираємо всі елементи в поточній директорії
    for item in src_dir.iterdir():
        if item.is_dir():
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            copy_files_recursively(item, dst_dir)
        elif item.is_file():
            # Отримуємо розширення файлу без крапки
            file_ext = item.suffix[1:]
            # Створюємо шлях для піддиректорії за розширенням файлу
            ext_dir = dst_dir / file_ext
            # Створюємо піддиректорію, якщо вона ще не існує
            ext_dir.mkdir(parents=True, exist_ok=True)
            # Копіюємо файл у відповідну піддиректорію, зберігаючи всі метадані
            shutil.copy(item, ext_dir / item.name)