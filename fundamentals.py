# Today we have a single warm up problem
# This was a practice problem from my notes from a Udmey course I took.
# See if you can break down the logic in this problem

#1 | Function

work_hours = [('Abby', 100), ('Billy', 200), ('Cassie', 400)]

def employee_check(work_hours):  #<<<<accepted list of tuples

    current_max = 0   #at the top of a function you normally have place holder variables
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

print(employee_check(work_hours))

result = employee_check(work_hours)

print(result)

#or as another return method

name,hours = employee_check(work_hours)

print(name)
print(hours)
