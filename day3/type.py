


# print(type(111) == type('str'))

class Student(object):
  def __init__(self,name):
    self.name = name

s = Student('zml')
s.age = 28
s.name = 'zhumingliang'

print(s.name,s.age)


class People(object):
  def run(self, fast):
    self.fast = fast
    # return self.fast
    print(self.fast)

xiaoming = People()
xiaoming.run(5)