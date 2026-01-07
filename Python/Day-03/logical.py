#logical AND
a = 10
b = 20
c = 30
if a > b and b > c:
    print("A is the largest number")
else:
    print("A is not the largest number")

#logical OR
a = 10
b = 20
c = 30 
if a > b or b < c:
    print("At least one condition is true")
else:
    print("Both conditions are false")

#logical NOT (or)
a = 10
b = 20
c = 30
if not (a < b or b < c):
    print("A is not greater than B")
else:
    print("A is greater than C")


#logical NOT (and)
a = 10
b = 20
c = 30
if not (a > b and b > c):
    print("A is not greater than B")
else:
    print("A is greater than C")


username = input("Enter username: ")
password = input("Enter password: ")
if username == 'sam' and password == 'sammy29':
    print("Login successful")
else:
    print("Login failed")