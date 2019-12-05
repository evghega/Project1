class Person:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


class Student(Person):
    def _init_(self, avrg, ins):
        self.average = avrg
        self.institute = ins


class Employee(Person):
    def __init__(self, salary):
        self.salary = salary


class WorkingStudent(Employee, Student):
    def __init__(self, same_institute):
        self.same_institude = same_institute


def main():
    size = int(input('Enter size for arr'))
    arr = []
    for i in range(size):
        type = input("Enter type of person(Student , Employee,WorkingStudent):")
        if type == "student":
            name = input("Enter name:")
            id = input("Enter ID:")
            age = input("Enter age:")
            avarage = input("Enter avareage:")
            institute = input("Enter intitute")
            arr[i] = Student(name, id, age, avarage, institute)
        if type == "Employee":
            name = input("Enter name:")
            id = input("Enter ID:")
            age = input("Enter age:")
            salary = input("Enter salary")
            arr[i] = Employee(name, id, age, salary)
        if type == "WorkingStudent ":
            name = input("Enter name:")
            id = input("Enter ID:")
            age = input("Enter age:")
<<<<<<< HEAD

            same_institute = input ("Enter same_institute")
            arr[i] = Student(name, id, age,same_institute)



main()
=======

            same_institute = input ("Enter same_institute")
            arr[i] = Student(name, id, age,same_institute)
>>>>>>> c14a6db1e9079f9396f64c346034cd594a1846dd

    