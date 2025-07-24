"""
i = 1
while i < 6:
    print(i)
    i += 1 #або можна записати так - i = i + 1

b = 43
while b < 56:
    print(b)
    if b == 53:
        break #зупиняє цикл навіть якшо умова тру
    b += 1

c = 0
while c < 6:
    c += 1
    if c == 3:
        continue # цей оператор зупиняє теперешній цикл і продовжує з наступного
    print (c)

a = 4
while a < 10:
    print(a)
    a += 1
else:
    print("а вже більше за 10")
"""
"""
friends = ["d3xis", "ars1k", "biscuit"]
for x in friends:
    print(x) # буде виводити елементи списку по 1

for a in "d3xis":
    print(a) # буде виводити букви рядка по 1

fruits = ["melon", "watermelon", "pineapple"]
for b in fruits:
    print(b) # буде виводити елементи списку до моменту зазначеного в умові if
    if b == "watermelon":
        break

stores = ["simi", "silpo", "salut", "atb"]
for c in stores:
    if c == "salut":
        continue #скіпає виконання цього циклу і переходить до наступного, тому код нижче не виконується
    print(c)
"""

"""
for x in range(6):
    print(x)

for c in range(2,6):
    print(c)


for v in range(2, 30, 3): # третє значення змінює послідовність. по дефолту 1
    print(v)
"""
"""
for x in range(6):
    print(x)
else:
    print("Операцію закінчено!")

for c in range(6):
    if c == 3:
        break
else:
    print("Закінчено!") # операція else не буде виконана після break, бо це обриває повністю весь цикл
"""
"""
rgb = ["red", "green", "blue"]
fruits = ["apple", "banana", "cherry"]

for x in rgb:
    for y in fruits: 
        print(x, y) # перший елемент х з кожним елементом у і так покі всі елементи х не виведуться
"""

for x in [0, 1, 2]:
    pass # для пустих циклів щоб пропустити виконання

"""
name = "d3xisars1kbiscuit"
name3 = ""
for x in name:
    name3 += x
    c = len(name3)
    if c % 3 == 0:
        print(name3)
"""
"""
name = "d3xisars1kbiscuit"
name3 = ""
r = -3
for x in name:
    name3 += x
    c = len(name3)
    if c % 3 == 0:
        r += 3
        print(name3[r:])
"""
""""
name = "d3xisars1kbiscuit"
name3 = ""
for x in name:
    name3 += x
    c = len(name3)
    if c % 3 == 0:
        print(name[::3]) # виводить кожен 3 індекс, в рендж так само 3 значення працює
        
"""
"""
name = "d3xisars1kbiscuit"
step = 3
for x in range(0, len(name), step):
    print(name[x:x+step]) 
"""
"""
name = "d3xisars1kbiscuit"
step = 3
i = 0
while i < len(name):
    print(name[i:i+step]) #кожен цикл в кінці до i додається 3(наш крок)
    i += 3
"""

"""
i = 1
total_costs = 0
while i < 6:
    costs = float(input(f"Введіть витрати за {i} день: "))
    total_costs += costs
    i += 1
print(total_costs)
"""

"""
total_costs = 0
for i in range(1, 6):
    costs = float(input(f"Введіть витрати за {i} день: "))
    total_costs += costs
print(total_costs)
"""
"""
cost_total = 0
while True:
    cost = input("Запишіть витрату: ")
    if not cost.isdigit():
        cost.lower()
        if cost == "stop":
            break  #завдання на майбутнє - як зробити так, щоб отримувати ввід float(може я даун і це тупа ідея)
    elif cost.isdigit():
        cost_int = int(cost)
        cost_total += cost_int
print(cost_total)
"""

"""
thislist_str = ["d3xis", "biscuit", "ars1k", "izzzumruuud"]
thislist_int = [1, 5, 7, 5, 9, 10]
thislist_any = [1, "fsd", 1.9, True]
list_any_method = list(("d3xis", "biscuit", "ars1k", "izzzumruuud"))
l = len(thislist_str)
print(thislist_str[1:], l, "\n", thislist_int, "\n", thislist_any)
print(type(thislist_int[0]))
print(list_any_method)
if "ars1k" in thislist_str:
    print("ars1k")
# в списках можна використовувати будь-які типи даних
# також 1 список може містити декілька типів даних
"""

"""
thislist = ["apple", "orange", "qiwi"]
thislist[1] = "banana" #таким способом можна змінювати елементи списку
thislist0 = ["gta", "minecraft", "metro", "god of war", "dark souls"]
thislist0[1:4] = ["steins;gate", "burnout", "genshin"]
thislist1 = ["gta", "minecraft", "metro", "god of war", "dark souls"]
thislist1[1:2] = ["mta", "trackmania"] # якщо вставити більше елементів чим замінюється, лишні елементи просто встануть після замінюваних
thislist2 = ["gta", "minecraft", "metro", "god of war", "dark souls"]
thislist2[1:5] = ["psp"] # якщо вставити менше елементів ніж замінюється, відсутні елементи просто видаляться зі списку
thislist3 = ["apple", "banana", "orange"]
thislist3.insert(0, "watermelon") # .insert() - вставляє новий елемент в список без заміни
thislist3.append("d3xis") # .append() - додає новий елемент в кінці списку
thislist3.extend(thislist0) # .extend() додає всі елементи з іншого списку в кінець цього списку
print(thislist, "\n", thislist0)
print(thislist1, "\n", thislist2, "\n", thislist3)
"""
"""
thislist = ["apple", "banana", "qiwi", "orange", "qiwi"]
thislist0 = ["apple", "banana", "qiwi", "orange", "qiwi"]
thislist1 = ["apple", "banana", "qiwi", "orange", "qiwi"]
thislist.remove("qiwi") # .remove() видаляє елемент зі списку. Якщо елементи повторюються, він видалить перший
thislist.pop(1) # видалить елемент за індексом
thislist.pop() # видалить останній елемент
del thislist[1] # видалить елемент за індексом
del thislist0 # видалить список повністю
thislist1.clear() # повністю очищує список, але не видаляє його
print(thislist, "\n", thislist1)
"""

"""
thislist = ["banana", "apple", "pomelo"]
for x in thislist:
    print(x) #буде виводити кожен елемент списку по черзі
for i in range(len(thislist)):
    print(thislist[i]) #буде виводити кожен елемент списку по черзі. range(3) - це індекси 0, 1, 2, 
                       # які кожен цикл будуть записуватись в і
"""
"""
thislist = ["banana", "apple", "pomelo"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
"""

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [z for z in fruits1 if "a" in z]
print(newlist)

newlist2 = [c for c in fruits1 if c != "apple"] # записує в змінну с елементи, якщо умова тру - додає елемент в список
print(newlist2)

newlist3 = [v for v in fruits1]
print(newlist3) #просто виводить всі елементи списку те саме що нижче:

newlist4 = []
for b in fruits:
    newlist4.append(b)
print(newlist4)

newlist5 = [n for n in range(10) if n < 5]
print(newlist5)
"""
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
"""
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["hello" for x in fruits]
print(newlist)
"""
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] # if х != banana - додати в x, else х буде orange - додати в х
print(newlist)
"""

"""
fruits = ["pomelo", "mango", "cherry", "kiwi", "banana"]
fruits.sort() # .sort() - сортує в алфавітному порядку по зростанню (за замовчуванням)
print(fruits)

fruits1 = ["pomelo", "mango", "cherry", "kiwi", "banana"]
fruits1.sort(reverse = True) # .sort() - сортує в алфавітному порядку по зростанню (за замовчуванням)
print(fruits1)

numbers = [42, 2, 49, 17, 6]
numbers.sort() # .sort() - сортує в цифри по зростанню (за замовчуванням)
print(numbers)

numbers1 = [42, 2, 49, 17, 6]
numbers1.sort(reverse = True) # .sort(reverse = True) - сортує в цифри по спаданню
print(numbers1)
"""



"""
def myfunc(n):
    return abs(n - 50) #Це функція, яка повертає різницю між числом n і числом 50 (n - число зі списку, яке сортується)
                       #і вже після цього сортує числа по зростанню різниці (самі числа зі списку не змінюються)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist1 = [30, 43, 20, 100, 90]
thislist1.sort(key = myfunc)
print(thislist1)

"""

"""
thislist1 = ["Orange", "apple", "banana", "Kiwi"]
thislist1.sort # за замовчуванням спочатку сортуються елементи з великої букви
print(thislist1)


thislist = ["Orange", "apple", "banana", "Kiwi"]
thislist.sort(key = str.lower) # ця ключ функція str.lower дозволяє провести сортування без чутливості до регістру
print(thislist)

thislist2 = ["Orange", "apple", "banana", "Kiwi"]
thislist2.reverse() # цей метод дозволяє сортувати список в зворотному порядку
print(thislist2)
"""

"""
thislist = ["Orange", "apple", "banana", "Kiwi"]
mylist = thislist.copy() # copy a list
print(mylist)
mylist1 = list(thislist) # another method copy
print(mylist1)
mylist2 = thislist[:] #last copy method
print(mylist2)
"""
"""
list1 = [1, "fsd", "apple"]
list2 = [443, 22, "apple"]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list4 = [1, "fsd", "apple"]
list4.extend(list2)
print(list1)

#ці всі методи роблять те ж саме, приєднують 1 список до другого
"""

expenses = []
amount3 = 0
while True:
    inp = input("Введи витрату: ")
    if not inp.isdigit():
        inp.lower()
        if inp == "stop":
            break
    if inp.isdigit():
        inp_int = int(inp)
        expenses.append(inp_int)
for i, amount in enumerate(expenses, start=1):
    amount3 += amount
    avg_expenses = amount3 / i
    print(f"{i}. {amount} грн")
print(f" Витрат взагалом: {amount3:.2f}", "\n", f"Середні витрати: {avg_expenses:.2f}")


# enumerate витягує значення і індекс з expenses і записує в вказані змінні

