#change value using key name
car = {'brand':'Audi','model':'q7'}
car['model']='A8'
print(car)

# update() method
car.update({'model':'A6'})
print(car)

# add items using key names
car['year']=2020
print(car)

# update() method to add items
car.update({'color':'red'})
print(car)