import csv
import matplotlib.pyplot as plt

with open("Data\Libraries_-_2017_Computer_Sessions_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

names = [x[0] for x in data] # grabbing list of library names (alphabetical)
names = names[1:] # chop off header
print(names)

ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd]
print(ytd)

ytd = [x for x in range(12)]  # just for testing. DELETE THIS LINE
month_number = [x for x in range(12)]
print(month_number)

# We want to plot computer users YTD vs library

plt.figure(1)
plt.plot(month_number, ytd)
plt.show()