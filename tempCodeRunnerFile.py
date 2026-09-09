def calculation(salary,bonus):
    total = salary + bonus
    return total

def final_salary(salary, bonus,tax):
    total = calculation(salary , bonus)
    result = total - tax
    return result

result = final_salary(25000, 5000 , 2000)
print(result)
