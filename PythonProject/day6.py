expenses = []
option = "0"

while True:
    if option == "0":
        print("Обери опцію: ", "\n", "1. Додати витрату", "\n", "2. Переглянути всі витрати", "\n", "3. Вийти")
        option = input()
    if option == "1":
        while True:
            expense = input("Введіть витрату: ")
            if expense.lower() == "stop":
                option = "0"
                break
            if expense.isdigit():
                expenses.append(float(expense))
            else:
                print("Це не число, спробуй ще раз")
    if option == "2":
        for i, amount in enumerate(expenses, start=1):
            print(f"{i}. {amount:.2f}")
        option = "0"
    if option == "3":
        print("Завершення програми")
        break
    if option == "0":
        continue
    else:
        print("ТИ ДАУН?")
        option = "0"
