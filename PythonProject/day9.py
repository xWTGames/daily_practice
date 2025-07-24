"""

def rectangle_area(a, b):
    return a * b

print(rectangle_area(17, 14))

print((lambda a, b: a * b)(17,14))


x = lambda a: a + 10
print(x(5))


def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 31))
print((lambda a, b: a if a > b else b)(10, 31))

x = lambda a: a * a

print(x(7))


numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x + 10, numbers) # map() функція, яка дозволяє застосувати функцію до кожного елемента списку, кортежу..
#
print(list(result))
"""

"""
def filt(x):
    return x % 5 == 0 # повертає значення true або false

numbers = [3, 10, 15, 20, 33, 40]
result0 = filter(filt, numbers)

# filter - функція, яка відбирає елементи в послідовності, які відповідають певній умові

print(list(result0))

result = filter(lambda a: a % 5 == 0, numbers) #функція, яка фільтрує елементи списку які діляться на 5

print(list(result))
"""
"""
products = [
    {"name": "Телефон", "price": 10000},
    {"name": "Телефон", "price": 15000},
    {"name": "Телефон", "price": 30000},
    {"name": "Телефон", "price": 1000},
    {"name": "Телефон", "price": 27000}
]

result = sorted(products, key= lambda products: products["price"] )
#сортує словники в списку за зростанням значення в ключі "price"

print(list(result))
"""

"""

print((lambda a, b: a + b)(17, 18))

words= ["яблуко", "банан", "вишня", "ківі", "апельсин"]

result = sorted(words, key = lambda words: len(words))
# сортує список за довжиною слів
print(list(result))


numbers = [4, -3, 9, 0, -1, 7, -8]

result1 = filter(lambda a: a < 0, numbers)
# фільтрує список тільки з негативними значеннями
print(list(result1))


prices_uah = [1000, 2500, 5000]

result2 = map(lambda a: a * 42, prices_uah)

print(list(result2))

"""

"""
def calc(a, b):
    return a - b

print(calc(17,10))

words= ["яблуко", "банан", "вишня", "ківі", "апельсин"]

def word_len(word):
    return len(word)

sorted_words = sorted(words, key = word_len)
print(sorted_words)


numbers = [-4, 13, 4, -3, -12]

def is_negat(x):
    return x < 0


filtered_numbers = filter(is_negat, numbers)
print(list(filtered_numbers))


prices_uah = [1000, 2500, 3500]

def calc_usd(x):
    return x * 42

result1 = map(calc_usd, prices_uah)

print(list(result1))
"""

#замість використання багато if..else. можна використовувати оператор match
#Як це працює:
# Вираз match оцінюється лише одного разу
# Значення виразу порівнюється з значенням в кожному case
# Якщо співпадіння знайдено код виконується
# match expression:
#   case x:

"""
day = 4

match day:
    case 1:
        print("Day 1")

    case 2:
        print("Day 2")

    case 3:
        print("Day 3")

    case 4:
        print("Day 4")

    case 5:
        print("Day 5")

    case 6:
        print("Day 6")

    case 7:
        print("Day 7")


match day:
    case 1:
        print("Day 1")

    case 2:
        print("Day 2")

    case 3:
        print("Day 3")

    case 5:
        print("Day 5")

    case 6:
        print("Day 6")

    case 7:
        print("Day 7")

    case _:
        print("В цьому тижні нема такого дня")

# _ в останньому значенні case виконає його код, якщо не знайдено інших співпадінь

month = 5
match day:
    case 1 | 2 | 3 | 4 if month == 4:
        print("А")
    case 1 | 2 | 3 | 4 if month == 5:
        print("В")
    case 6 | 7:
        print("С")

# | - використовується для запису більше 1 значення в case
# if в case використовується для перевірки на додаткову умову
"""
"""
day = input("Введіть день тижня: ")


def match_day(day):
    match day:
        case "Понеділок":
            print("Це робочий день")

        case "Вівторок":
            print("Це робочий день")

        case "Середа":
            print("Це робочий день")

        case "Четвер":
            print("Це робочий день")

        case "П'ятниця":
            print("Це робочий день")

        case "Субота":
            print("Це вихідний день")

        case "Неділя":
            print("Це вихідний день")


match_day(day)
"""
"""
cards = ["Visa", "Mastercard", "Amex", "Bitcoin", "PrivatPay"]

for x in cards:
    match x:
        case "Visa" | "Mastercard" | "PrivatPay":
            print(f"{x} - Класична платіжна система")

        case "Amex" | "Bitcoin":
            print(f"{x} - Нестандартна платіжна система")

        case _:
            print("У вас хуєсосбанк")

cards0 = ["Visa", "Mastercard", "Amex", "Bitcoin", "PrivatPay"]

cards_dict = [
    {"card": "Visa" , "type": "Класична система"},
    {"card": "Mastercard", "type": "Класична система"},
    {"card": "Amex", "type": "Нестандартна система"},
    {"card": "PrivatPay", "type": "Класична система"},
    {"card": "Bitcoin", "type": "Нестандартна система"}
]

for card in cards_dict:
    print(f"{card["card"]} - {card["type"]}")
"""

"""
data = [42, "hello", [1, 2, 3], 3.14, None]

for d in data:
    match d:
        case int():
            print("Ціле число")

        case str():
            print("Рядок")

        case list():
            print("Список")

        case float():
            print("Десяткове число")

        case None:
            print("None")

        case _:
            print("Невідомий тип")
"""

"""
fruit = ("orange",) # кортеж з 1 змінною
fruits = ("apple", "banana", "cherry")
fruits += fruit

(green, yellow, *red) = fruits #unpack tuple to variables.
# Кількість змінних повинна співпадати з кількістю значень у кортежі
# Якщо кількість змінних менша за кількість значень, можна використати *
# * - призначить до змінної значення які залишились списком


for i in range(len(fruits)):
    print(fruits[i])

mytuple = fruits * 2

print(green, yellow, red)
print(fruits)
print(mytuple)
"""

"""
myset = {"apple", "banana", "cherry"}
myset.add("orange")
tropical = {"papaya", "pineapple", "mango"}
myset.update(tropical)
mylist = ["origin", "steam", "uplay"]
myset.update(mylist) # не обов'язково об'єкт повинен бути сетом, можна додати елементи з будь-якого іншого об'єкту
print(myset)
"""

"""
myset = {"apple", "banana", "cherry", "mango"}
myset.remove("apple") # якщо цього елементу не існує - буде помилка
print(myset)
myset.discard("banana") # якщо цього елементу не існує - помилки не буде
print(myset)
myset.pop() #буде видаляти рандомний елемент
print(myset)

myset1 = {"apple", "banana", "cherry", "mango"}
myset1.clear()
print(myset1)

del myset1
"""
"""
myset = {"apple", "banana", "cherry", "mango"}
tropical = {"papaya", "pineapple", "mango"}
y = (1, 2, 3)

set_union = myset.union(tropical) #повертає новий сет зі всіма елементами обох сетів
set_1 = myset | tropical #повертає новий сет зі всіма елементами обох сетів

set_tuple = myset.union(y) #повертає новий сет зі всіма елементами кортежу і сету
# методом | об'єднувати можна тільки сети з сетами

print(set_union)

print(set_1)

print(set_tuple)
"""
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2) # вставляє всі елементи set2 в set1 включно з дублючимися

print(set1)
"""


"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) # повертає значення set1 і set2 але тільки дублікати
set4 = set1 & set2 # повертає значення set1 і set2 але тільки дублікати
print(set3)
print(set4)
"""
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2) #об'єднує дублікати set1 і set2
print(set1)
"""
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # поверне сет, який включає тільки елементи першого сету, які не присутні у іншому
set4 = set1 - set2 # поверне сет, який включає тільки елементи першого сету, які не присутні у іншому
print(set3)
print(set4)
"""

"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
"""
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2) #повертає всі елементи які не дублюються
set4 = set1 ^ set2 #повертає всі елементи які не дублюються
print(set3)
print(set4)
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2) #об'єднує всі елементи які не дублюються

print(set1)