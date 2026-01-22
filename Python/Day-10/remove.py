# Removes an item using pop() method
car = {'brand':'Audi','model':'q7','year':2020,'color':'red'}
car.pop('model')
print(car)

# Removes the item using popitem() method
car.popitem()
print(car)

# Removes an item using del keyword
del car['year']
print(car)  

# Removes a dictionary using del keyword
del car
  # This will raise an error since car is deleted

# Empty a dictionary using clear() method
car = {'brand':'Audi','model':'q7','year':2020,'color':'red'}
car.clear()
print(car)