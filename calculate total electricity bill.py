unit=(int(input("Enter the number of units consumed: ")))
if unit<=50:
    bill=unit*0.50
elif unit<=200:
    bill=50*0.50+(unit-50)*0.75
elif unit<=450:
    bill=50*0.50+150*0.75+(unit-200)*1.20
else:
    bill=50*0.50+150*0.75+250*1.20+(unit-450)*1.50
    final_bill=bill*1.20
    print("Final bill is",final_bill)
    
    