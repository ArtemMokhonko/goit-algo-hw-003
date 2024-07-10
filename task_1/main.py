from pathlib import Path
import sys
from file_operations import copy_files_recursively
from arg_parser import parse_args

def main():
    # Отримуємо аргументи командного рядка
    src_dir, dst_dir = parse_args()

    # Перевіряємо, чи існує вихідна директорія
    if not src_dir.exists():
        print(f"Вихідна директорія '{src_dir}' не існує.")
        sys.exit(1)

    # Створюємо директорію призначення, якщо вона ще не існує
    dst_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Викликаємо функцію для рекурсивного копіювання файлів
        copy_files_recursively(src_dir, dst_dir)
        print(f"Файли успішно скопійовані та відсортовані у '{dst_dir}'.")
    except Exception as e:
        # Виводимо повідомлення про помилку у разі винятку
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
