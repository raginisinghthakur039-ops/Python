for num in range(50):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz and Buzz ")
    elif num % 3 == 0:
        print("Fizz ")
    elif num % 5 == 0:
        print("Buzz ")
    else:
        print(num)