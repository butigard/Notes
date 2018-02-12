#LISTS AND LIST COMPREHENSION

my_list = ["Bev", "abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

# Using indices
print(my_list[3])
my_list[3] = "Deb"
print(my_list)

# Slicing
print(my_list[3:5]) # prints index 3 and 4
print(my_list[:4]) # beginning to 3
print(my_list[4:]) # 4 to end
print(my_list[:]) # prints the whole list

print("\n")

# Copying Lists
my_list_copy = my_list #NOT THIS WAY
my_list_copy[-1] = "Gob" # can use negative indices
print(my_list_copy)
print(my_list)

print("\n")

my_list_copy = my_list[:] # this copies the whole list into a new one
my_list_copy[-2] = "Feb" # can use negative indices
print(my_list_copy)
print(my_list)

print("\n")

# METHODS (AND FUNCTIONS) FOR LISTS

# finding out if an item exists in a list
print("Deb" in my_list)

# find the min and max of a list
print(min(my_numlist))
print(max(my_numlist))
print(sum(my_numlist))
print(min(my_list)) # alphabetical (sort of) goes by ordinal number
# print(ord("A"))

# find the index
print(my_list.index("Deb"))

print("\n")

# find how many times an item appears in a list
print(my_list.count("Gob"))

# add to a list
my_list.append("Gob")
print(my_list.count("Gob"))

# insert a value into a list
my_list.insert(3, "Don")
print(my_list)

# sort a list
my_list.sort()
print(my_list)

# reverse a list
my_list[my_list.index("abe")] = "Abe" # replace abe with Abe
my_list.reverse()
print(my_list)

# clear a list
my_list.clear()
print(my_list)

my_list = my_list_copy[:] # get my list back

# pop - removes an item from the list AND returns it
print(my_list)
removed_name = my_list.pop() #default removes the last item (pops it off)
print(my_list)
print(removed_name)

first_name = my_list.pop(0) # you can also index it
print(first_name)
print(my_list)

# delete an item from a list
del my_list[0]
print(my_list)
del my_list[1:]
print(my_list)

print("\n")

# ITERATING
# FOR EACH LOOP - Cannot change the list with this method
for item in my_numlist:
    item *= 2
    print(item)

print(my_numlist)

# Index variable LOOP - CAN change the list with this method
for i in range(len(my_numlist)):
    my_numlist[i] *= 2
    print(my_numlist[i])

print(my_numlist)

print("\n")

# CREATE LISTS
# Make a list of numbers 1 to 100
my_list = []
for i in range(1, 101):
    my_list.append(i)

print(my_list)

# Go back through the list and square everything
for i in range(len(my_list)):
    my_list[i] **= 2

print(my_list)