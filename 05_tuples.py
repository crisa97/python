# tuples
# the tuple the data not modificable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.70, "Cristhian", "Cruz", "Cruz")
my_other_tuple = (25, 35, 60)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) error IndexError

# count data of tuples
print(my_tuple.count("Cruz"))

# fiend data for index tuple
print(my_tuple.index("Cruz"))

# concat tuples in one 
print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# comber tuple a list 
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "crisa97"
my_tuple.insert(5, "black")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# remove tuple 
del my_tuple

# print(my_tuple) NameError: name 'my_tuple' is not defined