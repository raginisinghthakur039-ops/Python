# list=eval(input("Enter the list: "))
# print(list)
# print(type(list))
list=eval(input("Enter the list:"))
print(list)
for i in range (len(list)):
    if list[i]%2==0:
        list[i]+=5
    else:
        list[i]-=5
        
print(list)