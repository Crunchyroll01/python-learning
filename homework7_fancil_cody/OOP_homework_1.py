class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        # set private balance
        self._balance = float(initial_balance)
    # TODO: Set private _balance
    def deposit(self, amount):
        # TODO: Add amount if positive
        # Return new balance
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")
        return self._balance
    def withdraw(self, amount):
        # TODO: Subtract if sufficient funds
        # Print error if not
        # Return balance
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self._balance
        if amount > self._balance:
            print("Insufficient funds.")
            return self._balance
        self._balance -= amount
        return self._balance
    @property
    def balance(self):
        # TODO: Return _balance
        return self._balance
    def __str__(self):
        # TODO: Return formatted string
        return f"Account {self.account_number} owned by {self.owner}: balance ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        # TODO: Call parent constructor
        # TODO: Store interest_rate
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = float(interest_rate)
    def add_interest(self):
        # TODO: Calculate and add interest
        # Return interest amount
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest
    def withdraw(self, amount):
        # TODO: Check minimum balance of $100
        # Use parent's withdraw if ok
        min_balance = 100.0
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self._balance
        if self._balance - amount < min_balance:
            print(f"Cannot withdraw ${amount:.2f}: minimum balance of ${min_balance:.2f} must be maintained.")
            return self._balance
        return super().withdraw(amount)
    

# Test your code
if __name__ == "__main__":
    # Regular account
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")
    print("\n" + "="*40 + "\n")
    # Savings account
    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    # Try to go below minimum
    savings.withdraw(950) # Should fail
    savings.withdraw(500) # Should work
    print(f"Final balance: ${savings.balance}")