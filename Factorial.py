n= int(input("Enter the number: "))
def factorial(n):
    if n>=0:
        if n in [0, 1]:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        err= "Please Enter the positive integer"
        return err
print(factorial(n))