
accounts = []

class BankAccount ():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        while True:
            try:
                self.balance += int(input("Введіть суму поповнення: "))
                print(f"Ваш баланс: {self.balance} ")
                break
            except:
                print("Некоректне значення, спробуйте ще раз.")

    def withdraw(self):
        while True:
            try:
                if self.balance < 1:
                    print("На балансі немає коштів!")
                    break
                amount = int(input("Введіть бажану суму для зняття: "))
                if amount > self.balance:
                    print("Недостатньо коштів, введіть іншу суму.")
                else:
                    self.balance -= amount
                    print(f"Ваш баланс: {self.balance}")
                    break
            except ValueError:
                print("Некоректне значення, спробуйте ще раз.")

    def show_balance(self):
        print(f"Ваш баланс: {self.balance}")

class BankAccount_adm(BankAccount):
    def __init__(self, owner, balance, status): #коли ми в child класі створюємо init, клас більше не буде наслідувати батьківську init ф-цію
        super().__init__(owner, balance) # щоб зберегти батьківську ф-цію init, потрібно додати виклик батьківської init ф-ції
        self.status = status

def add_account():
    while True:
        owner = input("Введіть нікнейм акаунта: ")
        if owner.lower() == "stop":
            break
        accounts.append(BankAccount(owner, 0))

def add_adm_account():
    while True:
        password = input("Введіть пароль адміністратора: ")
        if password.lower() == "stop":
            break
        elif password == "12345":
            owner = input("Введіть нікнейм акаунта акаунта адміністратора:")
            accounts.append(BankAccount_adm(owner,0, "admin"))
        else:
            print("Невірний пароль, спробуйте ще раз.")

def show_main_menu():
    print(f"Виберіть опцію: \n 1. Додати новий акаунт. \n 2. Вибрати акаунт для керування. \n 3. Вийти з програми. \n 4. Додати акаунт адміністратора")
    return input("Введіть номер опції: ")

def show_manage_menu():
    print(f"Виберіть опцію: \n 1. Поповнити баланс. \n 2. Вивід коштів з балансу. \n 3. Переглянути баланс. \n 4. Вийти в головне меню. ")
    return input("Введіть номер опції: ")

def choose_user():
    print(f"Виберіть акаунт для керування: ")
    for i, x in enumerate(accounts, start=1):
        if hasattr(x, "status"):
            print(f"{i}. {x.owner} - {x.balance} {x.status}")
        else:
            print(f"{i}. {x.owner} - {x.balance}")
    while True:
        try:
            choice = int(input()) -1
            return accounts[choice]
        except (ValueError, IndexError):
            print("Невірне значення, спробуйте ще раз.")


while True:
    option = show_main_menu()

    if option == "1":
        add_account()

    elif option == "2":
        user = choose_user()
        while True:
            manage_option = show_manage_menu()
            if manage_option == "1":
                user.deposit()
            elif manage_option == "2":
                user.withdraw()
            elif manage_option == "3":
                user.show_balance()
            elif manage_option == "4":
                break
            else:
                print("Невірне значення, спробуйте ще раз.")

    elif option == "3":
        print("Завершення роботи програми. ")
        break

    elif option == "4":
        add_adm_account()

    else:
        print("Невірне значення, спробуйте ще раз.")


"""
accounts = []

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


def add_account():
    name = entry_name.get()
    if name:
        accounts.append(BankAccount(name))
        update_accounts_list()
        entry_name.delete(0, tk.END)

def update_accounts_list():
    listbox_accounts.delete(0, tk.END)
    for acc in accounts:
        listbox_accounts.insert(tk.END, f"{acc.owner} - Баланс: {acc.balance}")

def deposit_money():
    try:
        selected = listbox_accounts.curselection()[0]
        amount = float(entry_amount.get())
        accounts[selected].deposit(amount)
        update_accounts_list()
    except:
        messagebox.showerror("Помилка", "Виберіть акаунт і введіть число")

def withdraw_money():
    try:
        selected = listbox_accounts.curselection()[0]
        amount = float(entry_amount.get())
        if not accounts[selected].withdraw(amount):
            messagebox.showerror("Помилка", "Недостатньо коштів")
        update_accounts_list()
    except:
        messagebox.showerror("Помилка", "Виберіть акаунт і введіть число")

root = tk.Tk()
root.title("Monobank")
root.geometry("300x350")

tk.Label(root, text = "Ім'я користувача").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Button(root, text= "Додати акаунт", command=add_account).pack()

listbox_accounts = tk.Listbox(root, width=40)
listbox_accounts.pack()

tk.Label(root, text="Сума").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()
skklk
tk.Button(root, text="Поповнити", command=deposit_money).pack()
tk.Button(root, text="Зняти", command=withdraw_money).pack()

root.mainloop()

"""
