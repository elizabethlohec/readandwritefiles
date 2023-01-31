import csv
employee_pay=open('EmployeePay.csv', 'r')
employees=csv.reader(employee_pay, delimiter= ',')
next(employees)
for something in employees:
    salary=float(something[3])
    bonus=float(something[4])*salary
    total_pay=salary+bonus
    print("Name: " + something[1] +' ' + something[2])
    print("ID: " + something[0])
    print("Salary:" + str(salary))
    print("Bonus:" + str(format(bonus,'.2f')))
    print("Total Pay:" + str(total_pay))


