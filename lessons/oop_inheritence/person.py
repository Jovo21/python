class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age




class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)



class Doctor(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.salary = salary



    def davolash(self):
        print(f"Davolamoqda {self.name}")


    def __str__(self):
        return f"name: {self.name} age: {self.age} salary: {self.salary}"


    def infoDoctor(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"salary: {self.salary}")


class Teacher(Employee):

    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)


    def darsBeradi(self):
        print(f"Dars o'tmoqda {self.name}")