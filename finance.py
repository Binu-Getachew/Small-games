print("DEBUG: The script has started!")
import json
import datetime

class Transaction():
    def __init__(self,amount,category,description):
        self.amount=amount
        self.category=category
        self.description=description
        self.date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return{
            "amount":self.amount,
            "category":self.category,
            "description":self.description,
            "date":self.date
        }
    

class FinanceManager():
    def __init__(self, filename="wallet.json"):
        self.filename=filename
        self.data=self.load_data()

    def load_data(self):
        try:
            with open(self.filename,"r") as f:
                return json.load(f)
            
        except(FileNotFoundError, json.JSONDecodeError):
            return[]
        
    def add_entry(self,amount,category,description):
        new_tx=Transaction(amount,category,description)
        self.data.append(new_tx.to_dict())
        self.save()

    def save(self):
        with open(self.filename,"w") as f:
            json.dump(self.data,f,indent=4)

    def get_balance(self):
        return sum(item['amount'] for item in self.data)
    

def main():
    manager=FinanceManager()
    print("---Personal Finance Tracker---")

    while True:
        print("\n1. Add you income:")
        print("2. Add expenses")
        print("3. View current balance")
        print("4. View transaction history")
        print("5. Exit/Quit")

        choice=input("Choose an option:")

        if choice=='1':
            try:
                income_amount=float(input("Please enter the amount of income:"))
                income_category=input("Enter the category of your income:")
                income_descrpn=input("Please some description about it:")

                manager.add_entry(income_amount,income_category,income_descrpn)
                print("Transaction completed")

            except ValueError:
                print("Invalid input of value")

        elif choice=='2':
            try:
                expense_amount=float(input("Please enter the amount of expense:"))
                expense_category=input("Enter the category of your expenses:")
                expense_descrpn=input("Please some description about the expense:")

                manager.add_entry(-expense_amount,expense_category,expense_descrpn)
                print("Transaction completed")

            except ValueError:
                print("Invalid input of value")

        elif choice=='3':
            balance=manager.get_balance()
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == "4":
            print("\n--- History ---")
            for entry in manager.data:
                print(f"{entry['date']} | {entry['category']}: ${entry['amount']} ({entry['description']})")
                
        elif choice == "5":
            print("Saving data... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()




