
import shutil

def copy_files_recursively(src_dir, dst_dir):
    # Перебираємо всі файли у вихідній директорії та її піддиректоріях
    for path in src_dir.rglob('*'):
        if path.is_file():
            # Отримуємо розширення файлу без крапки
            file_ext = path.suffix[1:]
            # Створюємо шлях для піддиректорії за розширенням файлу
            ext_dir = dst_dir / file_ext
            # Створюємо піддиректорію, якщо вона ще не існує
            ext_dir.mkdir(parents=True, exist_ok=True)
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy2(path, ext_dir / path.name)


