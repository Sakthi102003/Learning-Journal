x = 10
y = x
y = 20
print(x)
print(y)

# copy() method
car = {'brand':'Audi','model':'q7','year':2020,'color':'red'}
car_copy = car
car_copy['model'] = 'A8'
print(car_copy)
print(car)

# Copying a dictionary using copy() method
car = {'brand':'Audi','model':'q7','year':2020,'color':'red'}
car_copy = car.copy()
print(car_copy)
car_copy['model'] = 'A8'
print(car_copy)

# Copying a dictionary using dict() method
car = {'brand':'Audi','model':'q7','year':2020,'color':'red'}
car_copy = dict(car)
print(car_copy)
car_copy['model'] = 'A8'
print(car_copy)
print(car)