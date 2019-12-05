class Person:
  def __init__(self, name,id, age):
    self.name = name
    self.id = id
    self.age = age


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