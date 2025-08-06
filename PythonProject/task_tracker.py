task_list = []

def show_menu():
    print(f"Виберіть опцію: \n 1. Додати завдання. \n 2. Показати список завдань. \n 3. Оновити завдання. \n 4. Видалити завдання. \n 5. Змінити статус завдання. \n 6. Показати завдання тільки в конкретному статусі.")
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
    task_list[choice]["text"] = task_text


def del_task():
    show_tasks()
    choice = get_task_index()
    task_list.pop(choice)

    for i, task in enumerate(task_list, start=1):
        task["id"] = i

    print("Завдання успішно видалено!")


def mark_task():
    show_tasks()
    choice = get_task_index()

    statuses = {
        "1": "виконано",
        "2": "в процесі",
        "3": "не виконано"
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
    while True:
        choice = input(
            f"Виберіть, який список завдань вивести: \n 1. Виконані \n 2. В процесі \n 3. Не виконані\nВаш вибір: "
        )
        statuses = {
            "1": "виконано",
            "2": "в процесі",
            "3": "не виконано"
        }

        if choice not in statuses:
            print("Невірне значення, спробуйте ще раз.")
            continue

        for t in task_list:
            if t["status"] == statuses[choice]:
                print(f"{t['id']}. {t['text']} - {t["status"]}")
        break


while True:
    option = show_menu()
    if option == "1":
        add_task()

    elif option == "2":
        show_tasks()

    elif option == "3":
        edit_task()

    elif option == "4":
        del_task()

    elif option == "5":
        mark_task()

    elif option == "6":
        specific_list()




