class Person:
  def __init__(self, name,id, age):
    self.name = name
    self.id = id
    self.age = age
<<<<<<< HEAD
    

class Student(Person):
	def _init_(self, avrg, ins):
		self.average=avrg
		self.institute=ins
		
======= """DONT TELL ME WHAT TO DO"""

class Employee(person):
    def __init__(self,salary):
        self.salary = salary

class WorkingStudent(Employee,Student):
  def __init__(self, same_institute):
    self.same_institude= same_institute
>>>>>>> e4ada1c28c46d718ed3ae934e619795b6528e5db
