"""
thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"] #також в словниках можуть бути списки
} #key: value повторення ключа перезапише минулий елемент
print(thisdict1)
print(len(thisdict1)) # довжиною буде кількість ключів

thisdict = dict(name = "d3xis", age = 43, country = "Norway") #dict(key = value)
print(thisdict)

x = thisdict1["model"] #доступ до елементу словника
print(x)

y = thisdict1.get("model") #або ще такий варіант, різниці 0
print(y)

z = thisdict.keys() #повертає список всіх ключів словника
print(z)
"""

"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}

x = car.keys()

print(x)

car["name"] = "for d3xis" #якщо такого ключа не існує він буде записаний в кінці словника

print(x)

y = car.values() # повертає всі значення словника
print(y)

z = car.items() # повертає кожен елемент словника
print(z)
"""

"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}
if "brand" in car: #перевіряє тільки присутність ключа, якщо це елемент - нічого не буде
    print("Yes, 'brand' is one of the keys in the car dictionary")

car.update({"year": 2020}) # але можна використати car["year"] = 2020

print(car["year"]) # виводить значення ключа year (2020)
"""

"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}

car.pop("colors") # видаляє елемент з вказаним ключом
car.popitem() #видаляє останній доданий елемент словника
del car["electric"] # видаляє елемент з вказаним ключом
del car # повністю видаляє словник

car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}

car1.clear() #повністю очищає словник
print(car1)

"""
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}

for x in car: #фор записує в х кожен ключ по порядку
    print(x) # виводить ключ з словника
    print(car[x]) # виводить значення елемента в ключі

for y in car.values():
    print(y) # виводить значення елемента
"""
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "white"]
}
for x, y in car.items(): # цей метод виводить повністю елемент словника, ключ і значення
    print(x, y)

car1 = car.copy() #метод копіювання словника
print(car1)

car2 = dict(car) #метод копіювання словника
print(car2)
"""

"""
myfamily = {
    "car1" : {
        "brand": "ford",
        "year": 2004
    },
    "car2" : {
        "brand": "audi",
        "year": 2010
    },
    "car3": {
        "brand": "bmw",
        "year": 2020
    }
} # словник з вкладеними трьома словниками


car1 = {
        "brand": "ford",
        "year": 2004
    }
car2 = {
        "brand": "audi",
        "year": 2010
    }
car3 = {
        "brand": "bmw",
        "year": 2020
    }

mycars = {
    "car1":car1,
    "car2":car2,
    "car3":car3
} #створює словник, який включає в себе 3 інснуючих словника

print(mycars, myfamily)
print(mycars["car1"]["brand"]) #доступ до елементів вкладеного словника

for keys, values in mycars.items():
    print(keys)

    for keys1 in values:
        print(keys1 + ":", values[keys1])



car5 = {
        "brand": "ford",
        "year": 2004
    }
for cars in car5:
    print(cars)
"""


balance = 0
option = "0"
transactions = []

def trans(trans_type, amount):
    global balance
    if trans_type == "дохід":
        balance += amount
    elif trans_type == "витрата":
        balance -= amount


def func0():
    global option
    print(f"Обери опцію: \n 1. Додати дохід \n 2. Додати витрату \n 3. Переглянути всі транзакції \n 4. Показати баланс \n 5. Вийти")
    option = input()

def func1():
    global option
    amount = input("Введи свій дохід: ")
    if amount.lower() == "stop":
        option = "0"
        return
    try:
        amount = float(amount)
        transactions.append({"type": "дохід", "amount": amount})
        trans("дохід", amount)
    except ValueError:
        print("Некоректне значення. Введи число або 'stop'.")

def func2():
    global option
    amount = input("Введи свою витрату: ")
    if amount.lower() == "stop":
        option = "0"
        return
    try: # isdigit() не вміє працювати з float. Тому при неправильному вводі спрацює виняток ValueError
        amount = float(amount)
        transactions.append({"type": "витрата", "amount": amount})
        trans("витрата", amount)
    except ValueError:
        print("Некоректне значення. Введи число або 'stop'.")

def func3():
    global option
    if transactions:
        print("Список транзакцій:")
        for i, t in enumerate(transactions, start=1):
            print(f"{i}. {t['type'].upper()} - {t['amount']}")
    option = "0"

def func4():
    global balance
    global option
    print(f"Поточний баланс: {balance:.2f}")
    option = "0"

while True:
    if option == "0":
        func0()

    elif option == "1":
        func1()

    elif option == "2":
        func2()

    elif option == "3":
        func3()

    elif option == "4":
        func4()

    elif option == "5":
        print("Завершення роботи програми.")
        break


