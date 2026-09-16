def calculate_basic_salary(employee):
    return employee["basic_salary"]

def calculate_hra(employee):
    hra = employee["basic_salary"] * 0.2
    return hra

def calculate_da(employee):
    da = employee["basic_salary"] * 0.1
    return da

def calculate_bonus(employee):
    if employee["experience"] >= 3:
        bonus = employee["basic_salary"] * 0.3
    elif employee["experience"] >= 2:
        bonus = employee["basic_salary"] * 0.2
    elif employee["experience"] >= 1:
        bonus = employee["basic_salary"] * 0.1
    else:
        bonus = 0
    return bonus

def calculate_tax(employee):
    tax = (employee["basic_salary"] + calculate_hra(employee) + calculate_da(employee) + calculate_bonus(employee)) * 0.18
    return tax

def calculate_net_salary(employee):
    net_salary = employee["basic_salary"] + calculate_hra(employee) + calculate_da(employee) + calculate_bonus(employee) - calculate_tax(employee)
    return net_salary