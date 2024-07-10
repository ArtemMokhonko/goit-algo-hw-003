import sys
from pathlib import Path
from copy_files import copy_files_recursively


def main():
    # Перевіряємо кількість аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python main.py вихідна_директорія директорія_призначення")
        sys.exit(1)

    # Отримуємо шлях до вихідної директорії з аргументів командного рядка
    src_dir = Path(sys.argv[1])
    # Отримуємо шлях до директорії призначення з аргументів командного рядка або встановлюємо за замовчуванням "dist"
    dst_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

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