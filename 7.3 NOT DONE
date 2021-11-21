class Account:
    def __init__(self, id, balance, annualInterestRate):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return "Account ID : {0.id} Account Ballance : {0.balance} Annual Interest Rate : {0.annualInterestRate}".format(self)

def main():
    accountA = Account(1122,2000,30)
    accountA.id = 1122
    accountA.balance = 20000
    accountA.annualInterestRate = 0.045
    print(accountA)
    accountA.withdraw(2500)
    accountA.deposit(3000)
    print(accountA)
    print(accountA.getMonthlyInterest()) 

main()
