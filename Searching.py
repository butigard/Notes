# SEARCHING

file = open('data/villains', 'r')  # open file to read (creates object named file)
print(file)

'''
for line in file:
    print(line)  # .strip() method removes spaces and \t \n from beginning and end
'''

for line in file:
    print("Hello", line.strip())

file.close()

# you can open a file to write (overwrite all previous)
#file = open('data/villains', 'w')
#file.write("Lee The Merciless")

# opena file to append (adds to the bottom of the file)
#file = open('data/villains', 'a')
#file.write("\nLee The Merciless")
#file.close()

# Read the file into a array (list)
file = open('data/villains', 'r')
villains = []
for line in file:
    villains.append(line.strip())

print(villains)

# Linear Search
key = "The Putrid Ogress"
i = 0
while i < len(villains) - 1 and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found", key, "at position", i)
