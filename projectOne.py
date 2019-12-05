class Person:
  def __init__(self, name,id, age):
    self.name = name
    self.id = id
    self.age = age


class WorkingStudent(Employee,Student):
  def __init__(self, same_institute):
    self.same_institude= same_institute