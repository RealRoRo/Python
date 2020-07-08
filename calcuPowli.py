
while True:
    a, b, c = input().split()
    a = float(a);
    c = float(c)
    if b == "+":
        print (a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        print(a/c)
    elif b == "%":
        print(a%c)
    elif b == "^":
        print(a ** c)
    else:
        print("Invalid operator")
    cont = input("Do you wnt to continue(y/n) : ")
    if cont == "n":
        break
