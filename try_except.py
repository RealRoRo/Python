

try:
    b = 10/0
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid number")
except ZeroDivisionError as err:
    print(err)