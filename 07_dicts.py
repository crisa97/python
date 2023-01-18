# dicts

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "name": "Cristhian",
    "surname": "Cruz",
    "age": 25, 1: "Python"
}

my_dict = {
    "name": "Cristhian",
    "surname": "Cruz",
    "age": 25,
    "languages": {"Python", "bash", "js"},
    1: 1.70
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# search

print(my_dict[1])
print(my_dict["name"])

print("Cruz" in my_dict)
print("surname" in my_dict)

# insert

my_dict["road"] = "road crisa97"
print(my_dict)

# update

my_dict["name"] = "Pedro"
print(my_dict["name"])

# remove

del my_dict["road"]
print(my_dict)

# others operations

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["name", 1, "Piso"]

# create dict any for keys
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("name", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "crisa97")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
