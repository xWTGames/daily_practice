"""
b = "d3xis"
print(b[:3]) #returns d3x

c = "d3xis"
print(c[1:4]) #returns 3xi

a = "d3xis"
print(a[1:]) #returns 3xis

z = ("d3xis")
print(z[-4:-2]) #returns 3x
"""
"""
ars1k = "BaRs1K"
print(ars1k.upper()) #returns BARS1K

bars1k = "ARS1K"
print(bars1k.lower()) #returns ars1k

d3x = "dexis"
d3x = d3x.upper()
print(d3x) #returns DEXIS

a = "   d3xis"
print(a.strip()) #returns "d3xis"

b = "d3xis"
print(b.replace("3", "e")) #returns dexis

c = "d3.xis"
print(c.split(".")) #returns 'd3', 'xis'. Сепаратором може бути не тільки крапка

x = "d3;xis"
print(x.split(";")) #returns 'd3', 'xis'
"""
"""
a = "ars1k"
b = "bars1k"
c = a + b
print(c) #return ars1kbars1k
print(a + b) #return ars1kbars1k
d = a + " " + b
print(d) #return ars1k bars1k

#txt = "arsik d3xis "fff" biscuit" #return error
txt = "arsik d3xis \"fff\" biscuit" #arsik d3xis "fff" biscuit
print(txt)

#escape characters:\", \", \\ (backslash), \n (new line), \r (carriage return), \t (tab), \b (backspace)
"""
""""
print(bool("Hello"))
print(bool(15))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#evaluation values.
#any strings is True, except empty strings
#any number is True, except 0
#any list, tuple, set, and dictionary are True, except empty ones

def myFunction():
    return True

print (myFunction())

def myFunction1():
    return False

if myFunction1():
    print("YES")
else:
    print("NO")
# за замовчуванням if - true

x = 200
print(isinstance(x, str)) #returns false
print(isinstance(x, int)) #returns true
#isinstance - функція, яку використовуют, щоб перевірити приналежність предмету до певного типу даних\

print(5>3) #returns True
"""

"""
a = 27
b = 27
if a == b:
    print(" a = b ")

c = 25
d = 36
if c == d:
    print("c = d")
elif c < d:
    print("c < d")

x = 25
v = 36
if x == v:
    print ("x = v")
else:
    if x < v:
        print("x < v")

if x < v: print("x < v")

print("A") if x < v else print("B")

"""
"""
a = 200
b = 33
c = 500
if a > b and c > a: #The and keyword is a logical operator, and is used to combine conditional statements
    print("Обидві умови True")
if a > b or a > c:
    print("Щонайменше одна умова True")
if not a < b: #якщо умова не true ми робимо цей код(по дефолту тру)
    print("a не быльше за b")
"""

"""
balance = float(input("Скільки в тебе грошей? "))
pokupka = float(input("Скільки коштує покупка? "))
left = pokupka - balance

if balance >= pokupka:
    print("Ти можеш це купити!")
else:
    print(f"У тебе не вистачає {left:.2f}")

"""

"""
cost = float(input("Введіть суму витрати: "))
if cost < 100:
    print("Невелика витрата")
elif cost >= 100 and cost < 1000:
    print ("Середня витрата")
else:
    if cost >= 1000:
        print("Велика витрата")
"""
"""
balance = float(input("Твій поточний баланc: "))
everyday_costs = float(input("Твої щоденні витрати: "))
days_to_next = int(input("Скільки днів залишилось до кінця місяця: "))

month_costs = everyday_costs * days_to_next
costs = month_costs - balance
if balance >= month_costs:
    print("Все ок!")
else:
    print(f"До кінця місяця не вистачить - {costs:.2f}")
"""

balance = float(input("Твій поточний баланc: "))
everyday_costs = float(input("Твої щоденні витрати: "))
days_to_next = int(input("Скільки днів залишилось до кінця місяця: "))

month_costs = everyday_costs * days_to_next
costs = month_costs - balance
if balance >= month_costs:
    print("Все ок!")
elif balance < month_costs:
    print(f"До кінця місяця не вистачить - {costs:.2f}")
    