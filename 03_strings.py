# strings

my_string = "My String"
my_other_string = 'My other String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "this is a string \nwith line break"
print(my_new_line_string)

my_tab_string = "\tthis is a string with tab"
print(my_tab_string)

my_scape_string = "\tthis is a string \nwith scape"
print(my_scape_string)

# Formate
print("____________________")
name, surname, age = "Cristhian", "Cruz", 25
# correct print 
print("My names is {} {} and my age is {}".format(name, surname, age))
print("My names is %s %s and my age is %s" %(name, surname, age))

# incorrect print
print("My name is " + name + " " + surname + " and my age is " + str(age)) 
# inference and formate or interpolation
print(f"My names is {name} {surname} and my age is {age}")

#unpacking
print("____________________")
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# division
print("____________________")
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)
# Reverse 
print("____________________")
reverse_language = language[::-1]
print(reverse_language)

# Function
print("____________________")
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())