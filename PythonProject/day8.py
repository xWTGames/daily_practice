import json

try:
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
        print(f"Знайдено {len(transactions)} транзакцій.")
except json.JSONDecodeError:
    print("Збережений файл зіпсований або пустий.")
    transactions = []


def calc(transactions):
    balance = 0
    for tx in transactions:
        if tx["type"] == "дохід":
            balance += tx["amount"]
        elif tx["type"] == "витрата":
            balance -= tx["amount"]
    return balance


def show_menu():
    print(f"Виберіть опцію: \n 1. Додати дохід. \n 2. Додати витрату. \n 3. Баланс. \n 4. Список транзакцій. \n 5. Вийти. \n")
    return input("Введи номер опції: ")

def add_transaction(transactions, trans_type):
    while True:
        amount = input(f"Введіть {trans_type}: ").lower()
        if amount == "stop":
            break
        try:
            amount = float(amount)
            transactions.append({"type": trans_type, "amount": amount})
            with open("transactions.json", "w", encoding="utf-8") as file:
                json.dump(transactions, file, ensure_ascii=False, indent=4)
        except ValueError:
            print("Ви ввели неправильне значення.")

def show_balance(transactions):
    balance = calc(transactions)
    print(f"Ваш баланс: \n {balance}")

def show_transactions(transactions):
    for t, amount in enumerate(transactions, start=1):
        print(f"{t}. {amount["type"].upper()} - {amount ["amount"]}")


while True:
    option = show_menu()

    if option == "1":
        add_transaction(transactions, "дохід")

    elif option == "2":
        add_transaction(transactions, "витрата")

    elif option == "3":
        show_balance(transactions)

    elif option == "4":
        show_transactions(transactions)

    elif option == "5":
        break
    else:
        print("Невірна опція. Спробуй ще раз.")


"""
x = '{ "name": "d3xis", "age": "20", "city": "Lutsk"}'

y = json.loads(x) #метод для парсингу json рядків

print(y["age"])
print(type(y))
"""
"""
x = { "name": "d3xis", "age": "20", "city": "Lutsk"}

y = json.dumps(x, indent=4) # конвертує об'єкт в json

print(y)
"""
"""
При конвертуванні в JSON ми будемо отримувати наступні типи даних:
dict - Object
list - Array
tuple - Array
string - String
int - Number
float - Number
True - true
False - false
None - null
"""



