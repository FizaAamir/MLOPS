class Wallet:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount

    def remove_balance(self, amount):
        self.balance -= amount

#you can put the test case here in main or make a separate file (test_main) 
# this is a test case:

# if __name__ == "__main__":
#     balance = wallet()
#     balance.addBalance(100)
#     balance.removeBalance(50)
#     assert balance.getBalance() == 50


# git branch -M main   
#COMMNADS TO UPLOAD TO GITHUB
    # git add -A
    # git commit -m "first commit"
    # push - u origin main 
