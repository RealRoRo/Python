def cube(number):
    return number ** 3


# num = int(input("Enter a number"))
# print("Cube of ",num,"is ",cube(num))

def isleap(year):
    if (year % 4 == 0):
        if year % 100 != 0 and year % 400 == 0:
            return False
        return True
    return False


# while True:
#     year = int(input("ENter yer"))
#     print(isleap(year))
#     cont =input("Do you want to continue  (y/n) :")
#     if cont == "n":
#         break


def sums(a, *b):  # pssing multiple values in func
    c = a
    print(a)
    print(b)
    for i in b:
        c = c + i
    print(c)


# sums(5, 6, 7, 8, 98)

def person(name, **data):
    print("Name: ", name)

    for i, j in data.items():
        print(i, ":", j)


# person("Ronak", age=19, city="Thrissur", number=8460088847)

def sum(a=0, b=0, c=0, d=0):
    return a + b + c + d

print(sum(1, 2, 7))
