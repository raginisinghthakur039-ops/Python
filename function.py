# when parameter is not passed in range
# when value is declared 0

    #write a programm which will add two number if number is even when calculate  even factorial
    #and number is odd when calculate odd factorial
# def factorial(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
#             return 10
# x= factorial(12)
# print(x)


def even_factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact
def odd_factorial(n):
    fact=1
    for i in range(1,n+1,2):
        fact*=i
    return fact
n=int(input("Enter the number:"))
if n%2==0:
    print("even number")
    print("Even factorial:", even_factorial(n))
else:
    print("odd number")
    print("Odd factorial:", odd_factorial(n))