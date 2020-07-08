class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    #overloading add
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)
        return m3

    #overload with __gt__(greater thAN)
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False

Student1 = Student(72, 23)
Student2 = Student(23, 34)

Student3 = Student1 + Student2  #ERROR SO overload with __add__
print("Marsk1 add",Student3.m1)
print("Marks2 add",Student3.m2)

if Student1 > Student2: #ERROR SO overload with __gt__(greater thAN)
    print("Student1 wins comp")
else:
    print("Student2 wins comp")

