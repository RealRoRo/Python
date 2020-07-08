a = 15
b = 20
def inFun():
    a = 9
    x = globals()['a']
    globals()['a'] = 20
    print("inside",a)

inFun()
print("outside",a)