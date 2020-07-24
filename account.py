from random import randint
from datetime import datetime

class Account:
    ''' Account Class to manage the creation of accounts '''

    def __init__(self, first_name, last_name, email, phone_number, account_type):
        ''' creates the neccesary attributes to manage and track account instance '''
        self.account_first_name = first_name.capitalize()
        self.account_last_name = last_name.capitalize()
        self.account_email = email
        self.account_phone_number = phone_number
        self.account_type = account_type

        self.account_pin = "0000"
        self.account_balance = 0.0
        self.account_number = self.generate_account_number()
        self.account_creation_timestamp = datetime.now()

    def __str__(self):
        response = "Account Info\n============\n"
        response += f"Name: {self.account_first_name} {self.account_last_name}\n"
        response += f"Number: {self.account_number}\n"
        response += f"Email: {self.account_email}\n"
        response += f"PhoneNumber: {self.account_phone_number}\n"
        response += f"Type: {self.account_type}\n"
        response += f"Balance: ₦{self.account_balance}k\n"
        return response

    def __repr__(self):
        return f"{self.account_first_name} {self.account_last_name}, {self.account_number}"


    def change_pin(self, new_pin):
        ''' change pin for the account instance '''
        self.account_pin = new_pin

    def check_balance(self):
        ''' returns the balance in the account instance '''
        return self.account_balance

    def generate_account_number(self):
        account_number = ''
        for i in range(10):
            new_digit = str(randint(0, 9))
            account_number += new_digit

        return account_number

    def deposit(self, amount):
        ''' increase the balance of the account instance '''
        self.account_balance += amount

    def transfer(self, other_account, amount):
        ''' increase and decrease the balance in account instance and other account instance respectively '''
        status = self.withdraw(amount)

        if status:
            other_account.deposit(amount)
            return True

        return False

    def withdraw(self, amount):
        ''' decrease the balance of the account instance '''
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

def run_tests():
    act1 = Account("sam", "loko", "sl@gmail.com", "07045273979", "current")

    assert act1.account_first_name == "Sam", f"{act1.__repr__()} firstname is not Sam"
    assert act1.account_last_name == "Loko", f"{act1.__repr__()} lastname is not Loko"
    assert act1.account_email == "sl@gmail.com", f"{act1.__repr__()} Email is not sl@gmail.com"
    assert act1.account_type == "current", f"{act1.__repr__()} Type is not current"
    assert act1.account_pin == "0000", f"{act1.__repr__()} Pin is not 0000"
    assert act1.account_phone_number == "07045273979", f"{act1.__repr__()} PhoneNumber is not 07045273979"

    assert act1.check_balance() == 0, f"{act1.__repr__()} balance is not 0"
    assert act1.deposit(100) is None, f"{act1.__repr__()} deposit Failed!"
    assert act1.check_balance() == 100, f"{act1.__repr__()} balance is not 100"
    assert act1.withdraw(50) is True, f"{act1.__repr__()} withdrawal Failed!"
    assert act1.check_balance() == 50, f"{act1.__repr__()} balance is not 50"

    act2 = Account("lola", "abegunde", "la@gmail.com", "07099999999", "savings")

    assert act2.account_first_name == "Lola", f"{act2.__repr__()} firstname is not Lola"
    assert act2.account_last_name == "Abegunde", f"{act2.__repr__()} lastname is not Abegunde"
    assert act2.account_email == "la@gmail.com", f"{act2.__repr__()} Email is not la@gmail.com"
    assert act2.account_type == "savings", f"{act2.__repr__()} Type is not savings"
    assert act2.account_pin == "0000", f"{act2.__repr__()} Pin is not 0000"
    assert act2.account_phone_number == "07099999999", f"{act2.__repr__()} PhoneNumber is not 07099999999"

    assert act2.check_balance() == 0, f"{act2.__repr__()} balance is not 0"
    assert act2.deposit(500) is None, f"{act2.__repr__()} deposit Failed!"
    assert act2.check_balance() == 500, f"{act2.__repr__()} balance is not 500"
    assert act2.transfer(act1, 250) is True, f"{act1.__repr__()} transfer Failed!"
    assert act2.check_balance() == 250, f"{act2.__repr__()} balance is not 250"

    assert act1.check_balance() == 300, f"{act1.__repr__()} balance is not 300"

    assert act2.change_pin("1234") is None, f"{act2.__repr__()} change pin failed!"
    assert act2.account_pin == "1234", f"{act2.__repr__()} Pin is not 1234"

    print("\n===================All tests Passed!================================\n")



def main():
    sample_account = Account("Jide", "Ariyo", "jd@semi.com", "09078345637", "savings")
    print("printing sample account")
    print(sample_account)

    print("printing sample account __str__")
    print(sample_account.__str__())

    print("printing sample account __repr__")
    print(sample_account.__repr__())

    run_tests()

if __name__ == "__main__":
    main()