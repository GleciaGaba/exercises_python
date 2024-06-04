class Person:
    def __init__(self, first_name, name, age):
        self.first_name = first_name
        self.name = name
        self.age = age

    def __bool__(self):
        return self.age > 18

    def __str__(self):
        return f"{self.first_name} {self.name}, {self.age}"


patrick = Person(first_name ="Patrick", name="TchuTchu", age=20)
john = Person(first_name="John", name="Snow", age=25)

print(patrick)
print(bool(john))

