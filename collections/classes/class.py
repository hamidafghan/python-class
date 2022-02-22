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
