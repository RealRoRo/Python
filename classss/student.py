
class Student:
    school = "K.K.M"

    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    @classmethod
    def info_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is blahblahblah")

    def print(self):
        print("name: ",self.name,
        "\nRoll no: ",self.roll, "\nAge: ",self.age)


student1 = Student("Ronak", 37, 19)
student2 = Student("amal", 21, 20)

student1.print()
student2.print()

print(Student.info_school())


