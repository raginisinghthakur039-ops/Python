year=int(input("Enter a year:"))
if year%100==0:
    if year%400==0:
        print("The year is a century year")
    else:
        print("The year is not a century year")