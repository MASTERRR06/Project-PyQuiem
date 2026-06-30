class SecondTime:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.is_now: bool = True

    def now(self):
        if self.is_now:
            print("ehh nvm " + str(self.name) + " " + str(self.age))
        else:
            self.is_now = False
            print("ehh nvm " + str(self.name) + " " + str(self.age))

    def __add__(self, other):#__add__: Defines what happens when you use the + operator to add objects together.
        return self.age + other.age

    def __str__(self):  # __str__: Defines what text displays when you pass an object to the print() function.
        return f"(Name={self.name}, Age={self.age})"


obj = SecondTime("Maira", 16)
print(obj)  # Now prints a clean string representation
