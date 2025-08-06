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

def get_task_index():
    while True:
        try:
            index = int(input("Виберіть завдання: ")) -1
            if 0<= index < len(task_list):
                return index
            else:
                print("Такого завдання не існує, спробуйте ще раз.")
        except ValueError:
            print("Невірне значення, спробуйте ще раз.")



def edit_task():
    show_tasks()
    choice = get_task_index()
    task_text = input("Запишіть оновлене завдання: ")
    task = {"id": choice,
            "text": task_text,
            "status": "не виконано"}
    task_list[choice] = task


def del_task():
    show_tasks()
    choice = get_task_index()
    task_list.pop(choice)
    print("Завдання успішно видалено!")

def mark_task():
    show_tasks()
    choice = get_task_index()

    statuses = {
        "1": "Виконано",
        "2": "В процесі",
        "3": "Не виконано"
    }
    while True:
        print("Виберіть, який статус призначити: \n 1. Виконано \n 2. В процесі \n 3. Не виконано")
        choice_status = input("Ваш вибір: ")
        if choice_status in statuses:
            task_list[choice]["status"] = statuses[choice_status]
            print("Статус успішно змінено!")
            break
        else:
            print("Невірне значення, спробуйте ще раз.")


def specific_list():
    choice = input(f"Виберіть, який список завдань вивести: \n 1. Виконані \n 2. В процесі \n 3. Не виконані")
    if choice == "1":
        for t in task_list:
            if t["status"] == "Виконано":
                print(f"{t["id"]}. {t["text"]} - {t["status"]}")
    elif choice == "2":
        for t in task_list:
            if t["status"] == "В процесі":
                print(f"{t["id"]}. {t["text"]} - {t["status"]}")
    elif choice == "3":
        for t in task_list:
            if t["status"] == "Не виконано":
                print(f"{t["id"]}. {t["text"]} - {t["status"]}")



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


