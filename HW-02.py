import os

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Попередження: рядок {line_number} має некоректний формат: {line}")
                    continue
                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
    
    return cats

# Отримати шлях до файлу на Робочому столі
desktop_path = os.path.expanduser("~/Desktop/cats_file.txt")


cats_info = get_cats_info(desktop_path)

# Виведення результату
print("Інформація про котів:")
for cat in cats_info:
    print(cat)