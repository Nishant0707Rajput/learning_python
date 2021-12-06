import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():           #------------->there is no self in it so static method.Can be called on class name
        val = datetime.datetime.utcnow()
        return pytz.utc.localize(val)

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance     # ----------> double underscores for mangling the names refer __dict__
        self.transaction_list = [(Account._current_time(), balance)]
        print(f"Account opened with name :- {name} with initial balance {balance}")
        # self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_list.append((Account._current_time(), amount))
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount should be less than available balance")
        self.show_balance()

    def show_balance(self):
        print(f"Your balance is {self.__balance}")

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount < 0:
                trans_type = "withdrawn"
                amount *= -1
            else:
                trans_type = "deposited"
            print(f"{amount:6} is {trans_type} on {date} local time was {date.astimezone()}")


if __name__ == '__main__':
    Nishant = Account("Nishant", 0)
    # Nishant.show_balance()
    #
    Nishant.deposit(2000)
    # Nishant.show_balance()
    Nishant.withdraw(500)
    # Nishant.show_balance()
    Nishant.show_transaction()

    Stephen = Account("Stephen", 800)
    Stephen.balance = 200   #-------------> new class attribute will be created, renamed as it may alter the data
    print(Stephen.__dict__)
    Stephen.deposit(100)

    Stephen.withdraw(200)
    Stephen.show_transaction()