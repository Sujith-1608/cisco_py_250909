# employees=[]
# emp1=("Sujith",22,40000)
# emp2=("Sinchana",22,50000)
# emp3=("rishika",22,48000)

# employees.append(emp1)
# employees.append(emp2)
# employees.append(emp3)

# print(employees)

# position=0
# search="Sinchana"

# for emp in employees:
#     if emp[0] == search:
#         break
#     position +=1

# print(position)

# salary=[1000,2000,2500,3000]

# # sal1=salary.pop(2500)

# # print(sal1)

# for i in range(len(salary)):
#     print(f"{i} : {salary[i]}")

employees=[]
emp1=("Sujith",22,40000,True)
emp2=("Sinchana",22,50000,True)
emp3=("rishika",22,48000,True)

employees.append(emp1)
employees.append(emp2)
employees.append(emp3)

print("Employees:",employees)

I=0
search="Sinchana"
index =-1

for emp in employees:
    if emp[0]==search:
        index=I
        break
    I +=1

if index ==-1:
    print('Employee not found')
else:
    search_employee=employees[index]
    print(search_employee)
    salary=float(input('Salary:'))
    employee=(search_employee[0],search_employee[1],salary,search_employee[3])
    employees[index]=employee
print('after search and update:', employees)

employee=('Dravid',50,200.75,True)
employees.append(employee)
print('after adding Dravid: ',employees)
employees.pop()

print('after delete Dravid: ',employees)

position=1
employees.pop(position)
print('after delete Sinchana: ',employees)
