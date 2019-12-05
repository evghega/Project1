class Person:
  def __init__(self, name,id, age):
    self.name = name
    self.id = id
    self.age = age
<<<<<<< HEAD
<<<<<<< HEAD


def main():
    size = input('Enter size for arr')
    arr=[]
    for i in range(size):
        type = input("Enter type of person(Studen , Employee,WorkingStudent):")
        if type == "student":
            name = input("Enter name:")
            id = input ("Enter ID:")
            age = input("Enter age:")
            avarage = input("Enter avareage:")
            institute = input("Enter intitute")
            arr[i]=Studen(name,id,age,avarage,institute)
        if type == "Employee":
            name = input("Enter name:")
            id = input("Enter ID:")
            age = input("Enter age:")
            salary = input("Enter salary")
            arr[i] = Studen(name, id, age,salary)
        if type == "WorkingStudent ":
            name = input("Enter name:")
            id = input("Enter ID:")
            age = input("Enter age:")
            same_institute = input ("Enter same_institute")
            arr[i] = Studen(name, id, age,same_institute)
=======
<<<<<<< HEAD
    
=======
>>>>>>> f84db2e376d89998aa0d545ddd79a19c63cb437c


    
class Student(Person):
	def _init_(self, avrg, ins):
		self.average=avrg
		self.institute=ins
<<<<<<< HEAD
		
======= 
=======


>>>>>>> aae4e1ec72c81d11d8c376a7b7553563cf8cca36

class Employee(person):
    def __init__(selcf,salary):
        self.salary = salary


        

class WorkingStudent(Employee,Student):
  def __init__(self, same_institute):
    self.same_institude= same_institute
<<<<<<< HEAD
>>>>>>> e4ada1c28c46d718ed3ae934e619795b6528e5db
>>>>>>> 1cd1849eda0c06a2973ca01cf984adef43cdfbb0
=======
>>>>>>> f84db2e376d89998aa0d545ddd79a19c63cb437c



<<<<<<< HEAD

=======

>>>>>>> a402b285acc5efc0e292cccd95e114a5acc1e629
