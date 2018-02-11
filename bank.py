class Bank(object):
	def __init__(self,account,balance):
		self.account=account
		self.balance=balance
	

	def withdraw(self,amount):
		self.balance=self.balance-amount
		return self.balance


	def deposit(self,amount):
		self.balance=self.balance+amount
		return self.balance

	def check_balance(self):
		print(self.balance)

ma = Bank(325243,2000)
print(ma.deposit(100))
print(ma.withdraw(300))
print(ma.balance)