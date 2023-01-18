# sets 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # initially is dict 

my_other_set = {"Cristhian", "Cruz", 25}
print(type(my_other_set))

# count data of set 
print(len(my_other_set))

my_other_set.add("crisa97")
print(my_other_set) # set not is structure ordered

my_other_set.add("crisa97")
print(my_other_set) # set not supports repeat data

# validate data in set 
print("Cristhian" in my_other_set)
print("cris" in my_other_set)

# delete data in set 
my_other_set.remove("Cristhian")
print(my_other_set)

# clear set is any
my_other_set.clear()
print(my_other_set)

# transformation
my_set = {"Cristhian", "Cruz", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# other operation

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))