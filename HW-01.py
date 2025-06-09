import os

def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                name, salary_str = parts
                try:
                    salary = float(salary_str)
                except ValueError:
                    continue
                total += salary
                count += 1
            if count == 0:
                return (0, 0)
            average = total / count
            return (total, average)
    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return (0, 0)

# Шлях до файлу на робочому столі (macOS)
desktop_path = os.path.expanduser("~/Desktop/path.txt")

# Виклик функції
total, average = total_salary(desktop_path)

# Вивід результату
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")