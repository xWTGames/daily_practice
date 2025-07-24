
fl_list = []
total_expenses = 0
expense = input("Введи витрати через кому в один рядок (напр. 100, 230, 45.5): ")
list_expenses = expense.replace(" ", "").split(",") #стріп тут не підійде, бо він видаляє пустоти тільки з боків
for i, value in enumerate(list_expenses, start=1):
    try:
        value = float(value)
        fl_list.append(value)
        total_expenses += value
    except ValueError:
        print(f"Помилка в елементі {i} -> '{value}' - пропущено.")
print("Список витрат: ")
for i, values in enumerate(fl_list, start=1):
    print(f"{i}. {values}")
print(f"Сума витрат: \n {total_expenses:.2f}")


"""
name = input("Введи своє ім'я: ")
age = input("Введи свій вік: ")
try:
    balance = float(input("Введи залишок на рахунку: "))
except ValueError:
    print("Некоректне значення!")
    balance = 0.0

print(f"Привіт, {name}! \n Тобі {age} років. \n На твоєму рахунку: {balance:.2f}")
"""