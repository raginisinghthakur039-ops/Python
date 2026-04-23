list1 = ["red", "yellow", "orange", "green", "white"]
list2 = ["black", "yellow", "green", "blue"]


# Find difference
difference = []

for item in list1:
    if item not in list2:
        difference.append(item)

print("Difference between list1 and list2:",difference)