lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

result = []
group = []

for i in lst:
    if group == [] or i == group[-1]:
        group.append(i)
    else:
        result.append(group)
        group = [i]

result.append(group)

print(result)