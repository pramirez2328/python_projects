'''
create a class called User with the following attributes:
_init_ method
add_name(),
add_age(),
add_email(),
add_username(),
add_password(),
user_login(),
__repr__()
user_info()

'''
from bank import Bank
import uuid
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog  # noqa: F401


class User(Bank):
    def __init__(self, name='', age='', email='', username='', password=''):
        super().__init__()
        self.holder_name = name
        self.age = age
        self.email = email
        self.username = username
        self.password = password

    def create_account(self) -> None:
        name = self.add_name()
        last = self.add_last()
        initial_amount = self.initial_amount()
        age = self.add_age()
        email = self.add_email()
        username = self.add_username()
        password = self.add_password()
        self.balance = initial_amount
        self.holder_name = f'{name} {last}'
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        self.account_number = uuid.uuid4().hex[:8]

    def save_account(self) -> None:
        self.accounts.append(
            {
                'name': self.holder_name,
                'balance': self.balance,
                'account_number': self.account_number,
                'age': self.age,
                'email': self.email,
                'username': self.username,
                'password': self.password,
            }
        )

    def add_name(self) -> str:
        name = tk.simpledialog.askstring(
            'Account creation',
            '* Enter your name:',
        )
        while True:
            try:
                for char in name:
                    if not char.isalpha():
                        raise ValueError
            except ValueError:
                msg.showerror('Error', 'Name must contain only letters')
                name = tk.simpledialog.askstring(
                    'Account creation',
                    '* Enter your name:',
                )
            else:
                break
        return name

    def add_last(self) -> str:
        last = tk.simpledialog.askstring(
            'Account creation',
            '* Enter your last name:',
        )
        return last

    def initial_amount(self) -> int:
        amount = tk.simpledialog.askinteger(
            'Account creation',
            '* Enter initial amount:',
        )
        return amount

    def add_age(self) -> int:
        age = tk.simpledialog.askinteger(
            'Account creation',
            '* Enter your age:',
        )
        return age

    def add_email(self) -> str:
        email = tk.simpledialog.askstring(
            'Account creation',
            '* Enter your email:',
        )
        return email

    def add_username(self) -> str:
        username = tk.simpledialog.askstring(
            'Account creation',
            '* Enter your username:',
        )
        return username

    def add_password(self) -> None:
        password = tk.simpledialog.askstring(
            'Account creation',
            '* Enter your password:',
        )
        return password

    def user_login(self, username, password) -> bool:
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def user_info(self) -> str:
        return f'\
        Account number: {self.account_number}\n\
        Name: {self.holder_name}\n\
        Balance: {self.balance}\n\
        Age: {self.age}\n\
        Email: {self.email}\n\
        Username: {self.username}\n\
        Password: {self.password}'


user1 = User()
user1.create_account()
user1.save_account()
print(user1.user_info())
print(user1.accounts)
