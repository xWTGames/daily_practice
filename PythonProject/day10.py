"""class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

"""


"""
class Person:
    def __init__(self, name, age): #селф це об'єкт, в нашому випадку p1
        self.name = name
        self.age = age
#ініт виконується автоматично кожен раз як клас використовується для створення нового об'єкту

p1 = Person("John", 36) # тут я створюю об'єкт і передаю значення в клас(name, age)


print(p1.name)
print(p1.age)
"""

"""
class InstagramAccount:
    def __init__(self, username, followers, following):
        self.username = username
        self.followers = followers
        self.following = following


user1 = InstagramAccount("d3xis", 199, 170)

print(user1.username)
"""
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
# Тут ми отримаємо якусь фігню. Щоб просто можна було ввести назву об'єкту і вивести потрібні данні
# потрібно використати функцію __str__() 
# або можемо через . вказати потрібну змінну (p1.name)

"""
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      return f"{self.name} {self.age}"

p1 = Person("John", 36)

print(p1)
"""
users = []

def show_menu():
    print(f"Виберіть опцію: \n 1. Додати підписників. \n 2. Переглянути список підписників. \n 3. Вийти.")
    return input("Введіть номер опції: ")

class InstagramAccount ():
    def __init__(self, username):
        self.followers = []
        self.username = username

    def follow(self):
        while True:
            self.follower = input("username follower ").lower()
            if self.follower == "stop":
                break
            else:
                self.followers.append({"follower": self.follower})
                print(f"Додано підписника {self.follower}")

    def show_followers(self):
        for i, x in enumerate(self.followers):
            print(f"{i}: {x}")


def add_user():
    while True:
        username = input("Введіть ім'я користувача: ")
        if username == "stop":
            break
        else:
            user = InstagramAccount(username)
            users.append(user)

def choose_user():
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.username}")
    while True:
        try:
            choice = int(input("Оберіть користувача за номером: ")) - 1
            return users[choice]
        except ValueError:
            print("Невірне значення")

add_user()
user1 = choose_user()

while True:
    option = show_menu()

    if option == "1":
        user1.follow()

    elif option == "2":
        user1.show_followers()

    elif option == "3":
        break
    else:
        print("Невірна опція, спробуй ще раз.")