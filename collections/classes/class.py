# Class
# python is a OOP language
# Class, function, properties, object

class Developer:
    # constructor
    def __init__(self, name, last_name, salary_per_hour):
        self.name = name
        self.last_name = last_name
        self.salary_per_hour = salary_per_hour

    # functions
    def full_name(self):
        return self.name + self.last_name

    def calculate_salary(self, hours, currency="Euro"):
        return str(self.salary_per_hour * hours) + " " + currency

# jamal = Developer("Jamal", "Kamal", 50)

# jamal.name = "Omid"

# # delete the object
# del jamal

# print(jamal)


# class SomeThing:
#     pass
# print("I am fine")

#  Getter and setter
class Student:
    __name = ""
    __last_name = ""

    def set_name(self, name):
        #  Some validations
        self.__name = name

    def get_name(self) -> str:
        return "MR. " + self.__name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self) -> str:
        return self.__last_name


student = Student()

#  Set the value
student.set_name("Kamal")
student.set_last_name("Jamal")

# Get the value
print(student.get_name())
print(student.get_last_name())
