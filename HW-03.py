import sys

from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = ""):
    """Рекурсивно виводить дерево директорій з кольорами"""
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: {path} не є директорією.")
        return

    entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        connector = "┣━" if index < entries_count - 1 else "┗━"
        if entry.is_dir():
            print(f"{prefix}{connector} {Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            print_directory_tree(entry, prefix + ("┃  " if index < entries_count - 1 else "   "))
        else:
            print(f"{prefix}{connector} {Fore.GREEN}{entry.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.")
        sys.exit(1)

    print(f"{Fore.CYAN}Структура директорії: {dir_path}\n")
    print_directory_tree(dir_path)

if __name__ == "__main__":
    main()