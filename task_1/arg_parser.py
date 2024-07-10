import sys
from pathlib import Path

def parse_args():
    """Парсить аргументи командного рядка і повертає шляхи до вихідної та призначеної директорій."""
    if len(sys.argv) < 2:
        print("Використання: python main.py <вихідна_директорія> [директорія_призначення]")
        sys.exit(1)

    # Отримуємо шлях до вихідної директорії з аргументів командного рядка
    src_dir = Path(sys.argv[1])
    # Отримуємо шлях до директорії призначення з аргументів командного рядка або встановлюємо за замовчуванням "dist"
    dst_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    return src_dir, dst_dir
