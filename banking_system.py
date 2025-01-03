#     **Description:**
#     Develop a console-based Banking System that allows users to create accounts, perform banking transactions, and manage their finances. The project should include secure login functionality, transaction logging, and persistent storage of user and transaction data using file handling.


import datetime
import os
import getpass

# Function to Create Account  < start >
def create_account():
    name = input("Enter your name: ")
    while True:
        try:
            initial_deposit = float(input("Enter your initial deposit: "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    account_number = generate_account_number()
    password = getpass.getpass("Enter your password: ")   # using getpass to encrypt the passowrd in command line .
    with open("accounts.txt", "a") as f:
        f.write(f"{account_number},{name},{password},{initial_deposit}\n")
    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully " + "\U0001F389")   # add some emojis for making better user experience .

# Function to Create Account < Closed >

# Function to Generate Account Numbers for user < start >

def generate_account_number():
    while True:
        # small code to check the entered accounnt number is only 6 digits 
        account_number = input("Enter a 6-digit number: ")
        if account_number.isdigit() and len(account_number) == 6: 
        # small code to check the entered accounnt number is only 6 digits 
            with open("accounts.txt", "r") as f:
                existing_accounts = {line.strip().split(",")[0] for line in f}
            if account_number in existing_accounts:
                print("Account number already exists." + "\U0001F494" +"\n\nPlease enter a different one.\n")
            else:
                return account_number
        else:
            print("Invalid input. Please enter a 6-digit number.")

# Function to Generate Account Numbers for user < end >

# Function to Login < start >
def login():
  account_number = input("Enter your account number: ")
  password = input("Enter your password: ")
  with open("accounts.txt", "r") as f:
    for line in f:
      data = line.strip().split(",")
      if data[0] == account_number and data[2] == password:
        print("Login successful!")
        return data
    print("Invalid account number or password.")
    return None
# Function to Login < start >

def deposit(account_data):
    while True:
        try:
            amount = float(input("Enter the deposit amount: "))
            if amount <= 0:
              print("Deposit amount must be positive.")
              continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    account_data[3] = str(float(account_data[3]) + amount)
    log_transaction(account_data[0], "Deposit", amount)
    update_accounts_file(account_data)
    print("Deposit successful!")

def withdraw(account_data):
    while True:
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                continue
            if amount > float(account_data[3]):
                print("Insufficient balance.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    account_data[3] = str(float(account_data[3]) - amount)
    log_transaction(account_data[0], "Withdrawal", amount)
    update_accounts_file(account_data)
    print("Withdrawal successful!")

def log_transaction(account_number, transaction_type, amount):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open("transactions.txt", "a") as f:
        f.write(f"{account_number},{transaction_type},{amount},{date}\n")

# Function to Update the account transactions in transaction.txt
def update_accounts_file(account_data):
    temp_data = []
    with open("accounts.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == account_data[0]:
                temp_data.append(",".join(account_data))
            else:
                temp_data.append(line.strip())
    with open("accounts.txt", "w") as f:
        for line in temp_data:
            f.write(line + "\n")

if not os.path.exists("accounts.txt"):
    with open("accounts.txt", "w") as f:
        pass

if not os.path.exists("transactions.txt"):
    with open("transactions.txt", "w") as f:
        pass

# User Control panel to interact with user 
while True:
    print("\n  Welcome to the Banking System \U0001F600\n===================================\n")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit" + "\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        account_data = login()
        if account_data:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Logout")
                transaction_choice = input("Enter your choice: ")
                if transaction_choice == "1":
                    deposit(account_data)
                elif transaction_choice == "2":
                    withdraw(account_data)
                elif transaction_choice == "3":
                    break
                else:
                    print("Invalid choice.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")