def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *=1
    return fact
def nCr(n,r):
    return factorial(n) // (factorial(r)*factorial(n-r))

n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
print(nCr(n,r))