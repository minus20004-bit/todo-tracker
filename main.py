# Финальная версия программы для практической работы
import os
import json

# Имя файла для хранения данных
FILENAME = "tasks.txt"

def load_tasks():
    """Загрузка задач из файла при старте программы"""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_tasks():
    """Сохранение текущих задач в файл"""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

# Загружаем задачи из файла в список
tasks = load_tasks()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=== КОНСОЛЬНЫЙ ТРЕКЕР ЗАДАЧ ===")
    print("1. Показать список задач")
    print("2. Добавить новую задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Выйти из программы")
    print("===============================")

def list_tasks():
    clear_screen()
    if not tasks:
        print("Ваш список задач пуст! 🎉\n")
        return
    
    print("--- ТЕКУЩИЕ ЗАДАЧИ ---")
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")
    print("----------------------\n")

def add_task():
    clear_screen()
    title = input("Введите название задачи: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks()  # Сохраняем изменения
        print(f"Поставлена задача: \"{title}\" ➕\n")
    else:
        print("Название задачи не может быть пустым!\n")

def complete_task():
    list_tasks()
    if not tasks:
        return
    try:
        num = int(input("Введите номер выполненной задачи: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks()  # Сохраняем изменения
            print("Статус задачи обновлен! Число дел уменьшается. 🚀\n")
        else:
            print("Неверный номер задачи!\n")
    except ValueError:
        print("Пожалуйста, введите корректное число.\n")

def delete_task():
    list_tasks()
    if not tasks:
        return
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()  # Сохраняем изменения
            print(f"Задача \"{removed['title']}\" удалена. 🗑️\n")
        else:
            print("Неверный номер задачи!\n")
    except ValueError:
        print("Пожалуйста, введите корректное число.\n")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("До встречи! Продуктивного дня! 👋")
            break
        else:
            clear_screen()
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.\n")

if __name__ == "__main__":
    main()
