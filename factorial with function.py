def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

    """
    pass the factorial
    """

number = int(input("Enter a number:"))

print(factorial(number))

x, y = input(), input()
print("x=",x,"y=",y)

# Read two numbers from input and typecasts them to int using
# list comprehension
x, y = [int(x) for x in input().split()]

