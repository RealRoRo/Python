class A:
    def fun1(self):
        print("This is fun1")

    def fun2(self):
        print("This is fun2")


class B:
    def fun1(self):
        print("ksdjdcbksjbdsb")

    def fun4(self):
        print("This is fun4")


class C(B, A):
    def fun5(self):
        print("This is fun5")

    def fun6(self):
        print("This is fun6")


aobj = A()
bobj = B()
cobj = C()

# aobj.fun1()
# bobj.fun3()
cobj.fun1()
