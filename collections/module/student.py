config = {
    "version" : 1,
    "last_update": "Today"
}


def getVersion():
    return config["version"]

class Student:
    def __init__(self, name, last_name, year) -> None:
        self.name = name
        self.last_name = last_name
        self.year = year

    def getClass(self):
        return int(self.year)

    def full_name(self):
        return str(self.name) + " "+ str(self.last_name)
