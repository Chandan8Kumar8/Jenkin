class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    print("id:",self.id)
    Employee.new_id += 1
    print(Employee.new_id)

  def say_id(self):
    print("My id is {}.".format(self.id))

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()