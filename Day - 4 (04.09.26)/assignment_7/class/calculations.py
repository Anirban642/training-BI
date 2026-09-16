class Employee:
    def __init__(self, name, basic_salary, experience):
        self.name = name
        self.basic_salary = basic_salary
        self.experience = experience

    def calculate_basic_salary(self):
        return self.basic_salary

    def calculate_hra(self):
        hra = self.basic_salary * 0.2
        return hra

    def calculate_da(self):
        da = self.basic_salary * 0.1
        return da

    def calculate_bonus(self):
        if self.experience >= 3:
            bonus = self.basic_salary * 0.3
        elif self.experience >= 2:
            bonus = self.basic_salary * 0.2
        elif self.experience >= 1:
            bonus = self.basic_salary * 0.1
        else:
            bonus = 0
        return bonus                

    def calculate_tax(self):
        tax = (self.basic_salary + self.calculate_hra() + self.calculate_da() + self.calculate_bonus()) * 0.18
        return tax
        
    def calculate_net_salary(self):
        net_salary = (self.basic_salary + self.calculate_hra() + self.calculate_da() + self.calculate_bonus() - self.calculate_tax())
        return net_salary
