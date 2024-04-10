"""
dict_practice.py

In this exercise you will practice with dictionary methods

Follow the instructions below
"""

# make a dictionary that called number_names that stores as 
# keys the numbers from 1 to 5 in words, and as values the integers themselves
# so, an example of an entry would be where the key is 'two' and the value is 2
number_names={"one":1, "two":   2}

# get the value corresponding to the key 'two'

print(number_names["two"])



# get a list of all the keys in this dictionary

key_list=[]


for key in number_names:
    key_list.append(key)
    
print(key_list)

# get a list of all the values in this dictionary

value_list=[]

for key in number_names:
    value_list.append(number_names[key])
    print(key) 
   
for i in range(4):
    print(i)
    for j in range(4):
        print(j)
     

# delete the last entry of the number_names

number_names.popitem()


# remove the 'two' entry
number_names.pop

print(number_names)



# count the number of entries and print this out
# again, do this programmatically! we are not testing if you can count ;)


# delete all the values from the dictionary, what do you get?

