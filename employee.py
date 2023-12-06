"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

#check what type of contract worker is: salary or hourly contract
#if salary contract, they earn monthly salary
#if hourly contract, earn hourly wage * num of hours worked

#next check if they receieve commission
#two types of commission: check which type
#commission based on num of contracts they have landed:
#num of contracts landed * commission per contract
#OR fixed bonus addition

#total pay = contract pay + commission if any


class Employee:
    def __init__(self, name, contract_type, pay_type, commission_type=None, commission_amount=None, hours_worked=None, num_of_contracts=None):
        self.name = name
        self.contract_type = contract_type
        self.pay_type = pay_type
        self.commission_type = commission_type
        self.commission_amount = commission_amount
        self.hours_worked = hours_worked
        self.num_of_contracts = num_of_contracts

    def get_pay(self):
        if self.contract_type == "Salary":
            contract_pay = self.pay_type
        elif self.contract_type == "Hourly":
            contract_pay = self.pay_type * self.hours_worked
        else:
            raise ValueError("Invalid contract type!")

        commission_pay = 0
        if self.commission_type == "Bonus":
            commission_pay = self.commission_amount
        elif self.commission_type == "Contract":
            commission_pay = self.commission_amount * self.num_of_contracts

        return contract_pay + commission_pay

    def __str__(self):
        contract_str = f"{self.name} works on a "
        if self.contract_type == "Salary":
            contract_str += f"monthly salary of {self.pay_type}"
        elif self.contract_type == "Hourly":
            contract_str += f"contract of {self.hours_worked} hours at {self.pay_type}/hour"

        commission_str = ""
        if self.commission_type == "Bonus":
            commission_str += f" and receives a bonus commission of {self.commission_amount}"
        elif self.commission_type == "Contract":
            commission_str += f" and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_amount}/contract"

        return f"{contract_str}{commission_str}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'Salary', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'Hourly', 25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'Salary', 3000, 'Contract', 200, num_of_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'Hourly', 25, 'Contract', 220, hours_worked=150, num_of_contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'Salary', 2000, 'Bonus', 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'Hourly', 30, 'Bonus', 600, hours_worked=120)


print(billie.get_pay())  
print(str(billie)) 

print(charlie.get_pay())  
print(str(charlie)) 

print(renee.get_pay())  
print(str(renee))

print(jan.get_pay())  
print(str(jan))  

print(robbie.get_pay()) 
print(str(robbie))  

print(ariel.get_pay())  
print(str(ariel))