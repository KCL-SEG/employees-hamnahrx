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
    def __init__(self, name, contract_type, salary=0, hourly_rate=0, hours_worked=0, commission=False, commission_type="", bonus=0, num_of_contracts=0, commission_per_contract=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.commission = commission
        self.commission_type = commission_type
        self.bonus = bonus
        self.num_of_contracts = num_of_contracts
        self.commission_per_contract = commission_per_contract


    def get_pay(self):
        if self.contract_type == "monthly":
            pay =  self.salary
        elif self.contract_type == "hourly":
            pay = self.hours_worked * self.hourly_rate
        else:
            pay = 0

        if self.commission == True:
            if self.commission_type == "bonus":
                pay += self.bonus
            elif self.commission_type == "contract":
                pay += self.num_of_contracts * self.commission_per_contract
        
        return pay

    def __str__(self):
        if self.contract_type == "monthly" and self.commission == False:
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "monthly" and self.commission == True and  self.commission_type == "bonus":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}"
        elif self.contract_type == "monthly" and self.commission == True and self.commission_type == "contract":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}"
        elif self.contract_type == "hourly" and self.commission == False:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.commission == True and self.commission_type == "bonus":
            return f"{self.name} works on a contract of {self.hours_worked}/hours and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}"
        elif self.contract_type == "hourly" and self.commission == True and self.commission_type == "contract":
            return f"{self.name} works on a contract of {self.hours_worked}/hours at {self.hourly_rate}/hour and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hourly_rate=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', salary=3000, commission=True, commission_type='contract', num_of_contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', hourly_rate=25, hours_worked=150, commission=True, commission_type='contract', num_of_contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', salary=2000, commission=True, commission_type='bonus', bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', hourly_rate=30, hours_worked=120, commission=True, commission_type='bonus', bonus=600)
