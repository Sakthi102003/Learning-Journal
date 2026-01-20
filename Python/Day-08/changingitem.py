list = ["user1", "user2", 1,2, "user3"]
list[1] = "user4"

#changing multiple items
list[2:4] = ["user4", "user5", "user6"]


#insert items
list.insert(2, "user7")
print(list)