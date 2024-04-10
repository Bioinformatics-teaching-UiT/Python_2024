"""
list_practice.py

In this exercise, you will practice the most common list methods.

Write your lines of code under each comment.
"""

# create a list named 'numbers' with the integers 1 to 8
number = [1,2,3,4,5,6,7,8]
# add 9 to the end of the list

# add the extension to the end of your numbers list


# print out an informative message that gives the number of 
# elements in the list, and then the list itself
# no hard coding! (don't count in your head and print it, 
# have the code count for you)

print(f"The list of numbers has {len(number)} entries")

# here is a list, can you print out how many times 'dog' occurs?
animals = ['cat', 'rat', 'mouse', 'dog', 'giraffe', 'dog']



animals.count("dog")

count = 0

for animal in animals:
    if animal == "dog":
        count += 1 
        
print(count)


# insert a moose at the first position of the animals list



# using the remove() method, remove 'dog' - 

animals.remove("dog")


for animal in reversed(animals):
    print(animal)
    if animal =="dog":
        animals.remove(animal)


print(animals)
    

# check the list - is this the behaviour you expect?

# pop out the 3rd element, what do you get?

single_animal=animals.pop(2)
print(single_animal)

# reverse the animal list

animals.reverse
rev_animals=animals[::-1]
print(animals


# clear the animal list, what do you get?

animals.clear()
print(animals)

