# Parent class, child calss
# Remove duplicate code/logics

class Human:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    def full_name(self):
        return self.name + " " + self.last_name


class Employee:
    def __init__(self, per_hour) -> None:
        self.per_hour = per_hour

    def calculate_salary(self, hours):
        return self.per_hour * hours


class Developer(Human, Employee):
    def __init__(self, name, last_name, per_hour) -> None:
        Human.__init__(self, name, last_name)
        Employee.__init__(self, per_hour)


jamal = Developer("Jamal", "Kamal", 50)

print(jamal.calculate_salary(30))
