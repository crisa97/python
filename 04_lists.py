# lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [25, 35, 24, 62, 52, 30 , 30 , 17]

print(my_list)
print(len(my_list))

my_other_list = [25, 1.70, "cristhian", "cruz"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])

print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] 
print(age)

# concat the list 
print(my_list + my_other_list)

print(list([1, 2, 3, 4]))

# add in list in final
my_list.append("Hi python")
print(my_list)

# add to star 
my_list.insert(1, "Red")
print(my_list)

# replace the list value
print("___________________")
my_list[1] = "Black"
print(my_list)
print("___________________")

# remove to index in list
my_list.remove("Black")
print(my_list)

my_other_list.remove("cristhian")
print(my_other_list)

# remove the last one from the list  and return list

print("___________________")
my_list.pop()
print(my_list)

# remove for element of list
my_pop_element = my_list.pop(2)
print(my_pop_element)

print("___________________")

# remove for index
del my_list[2]
print(my_list)

# copy list 
my_new_list = my_list.copy()
print(my_new_list)

# clear list is any
print("___________________")
my_list.clear()
print(my_list)
print("___________________")

# reverse to list in order 
my_new_list.reverse()
print(my_new_list)

# order list in  < >
my_new_list.sort()
print(my_new_list)

#sub list
print(my_new_list[1:2])

my_list = list("hi crisa97")
print(my_list)
print(type(my_list))