class Person:
  def __init__(self, name,id, age):
    self.name = name
    self.id = id
    self.age = age
    

class Student(Person):
	def _init_(self, avrg, ins):
		self.average=avrg
		self.institute=ins
		