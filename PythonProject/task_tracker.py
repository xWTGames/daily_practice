task_list = []

def show_menu():
    print(f"Виберіть опцію: \n 1. Додати завдання. \n 2. Показати список завдань. \n 3. Оновити завдання. \n 4. Видалити завдання. \n 5. Змінити статус завдання.")
    return input("Введіть номер опції: ")

def add_task():
    task_text = input("Запишіть завдання: ")
    task = {"id":len(task_list) +1,
            "text": task_text,
            "status": "не виконано"}
    task_list.append(task)
    print("Завдання записано!")

def show_tasks():
    print("Список завдань: ")
    for t in task_list:
        print(f"{t["id"]}. {t["text"]} - {t["status"]}")

def edit_task():
    show_tasks()
    choice = int(input("Виберіть завдання для оновлення: ")) -1
    task_text = input("Запишіть оновлене завдання: ")
    task = {"id": choice,
            "text": task_text,
            "status": "не виконано"}
    task_list[choice] = task

def del_task():
    show_tasks()
    choice = int(input("Виберіть завдання, яке бажаєте видалити: ")) -1
    task_list.pop(choice)

def mark_task():
    show_tasks()
    choice = int(input("Виберіть завдання, якому бажаєте змінити статус: ")) - 1
    mark = input("Напишіть статус завдання: ")
    task_list[choice]["status"] = mark
    print("Статус успішно змінено!")



while True:
    option = show_menu()
    if option == "1":
        add_task()

    if option == "2":
        show_tasks()

    if option == "3":
        edit_task()

    if option == "4":
        del_task()

    if option == "5":
        mark_task()


