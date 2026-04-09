num = 12

evencount =0
oddcount =0
for i in range(1, num + 1):
   if num % i ==0:
    if i%2 ==0:
        evencount += 1
    
    else:
        oddcount += 1 
print("Even factors:", evencount)
print("Odd factors:", oddcount)