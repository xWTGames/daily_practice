
"""
типи даних
x = 1j #complex

y = ["aa", "bb", "cc"] #list

z = ("aa", "bb", "cc") #tuple

q = {"name" : "John", "age" : 36} #dict

p = {"aa", "bb", "cc"} #set

i = range(6) #range
"""

"""
x = 1
z = 1.0

a = float(x)
b = complex(x)
c = int(z)

print(a, b, c)

print(type(a))
print(type(b))
print(type(c))

"""

"""
import random

print(random.randrange(1, 10))

"""
"""
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
"""
#мультирядковий рядок
#a = """Lodsalfs ldasdf,
#flsflffs dlslfdsd;
#fdsfld;a;f"""
#print(a)

#вивід конкретного елементу з масиву або з рядка.
#рахунок починається з 0
#a = "ars1k27"
#print(a[5:7])

#for x in "banana":
#    print(x)
"""
#довжина рядка
a = "d3xis"
x = len(a)
print(len(a))
print(x)
"""
"""
#перевірка присутності певних слів/символів у рядку. Повертає bool значення
txt = "ars1k, bars1k, biscuit"
print("bars1k" in txt)
"""

"""
#print only if bars1k is present
txt = "ars1k, bars1k, biscuit"
if "bars1k" in txt:
    print("bars1k is here")
"""

"""
#check if d3xis not present in text
txt = "ars1k, bars1k, biscuit"
print("d3xis" not in txt)
"""

"""
txt = "ars1k, bars1k, biscuit"
if "d3xis" not in txt:
    print("d3xis is not here")
"""
"""
#КОМБІНУВАТИ ЦИФРИ І РЯДКИ МИ НЕ МОЖЕМО,
#ДЛЯ ЦЬОГО ПОТРІБНО ВИКОРИСТОВУВАТИ ФОРМАТОВАНІ РЯДКИ (F-Strings)
age = 36
#txt = "I am " + age #так не вийде
txt = f"I am {age} years old"
print(txt)
"""
"""
price = 1203.4285564
txt = f"The price is {price:.2f} dollars"
print(txt)
"""


income = float(input("Введи свій дохід за день (грн): "))
food = float(input("Скільки ти витрачаєш на їжу за день? "))
transport = float(input("Скільки ти витрачаєш на транспорт за день? "))
other =  float(input("Інші витрати за день "))

income_week = float(income * 7)
food_week = float(food * 7)
transport_week = float(transport * 7)
other_week = float(other * 7)

total_expenses = food + transport + other
balance = income - total_expenses

total_expenses_week = food_week + transport_week + other_week
balance_week = income_week - total_expenses_week

print(f"Загальні витрати за день: {total_expenses:.2f} грн")
print(f"Залишок за день: {balance:.2f} грн")
print(f"Загальні витрати за тиждень: {total_expenses_week:.2f} грн")
print(f"Залишок за тиждень: {balance_week:.2f} грн")

daily_cost = total_expenses
days = balance_week // daily_cost
leftover = balance_week % daily_cost

print(f"На залишок за тиждень можна прожити {int(days)} днів, залишиться {leftover:.2f} грн")


