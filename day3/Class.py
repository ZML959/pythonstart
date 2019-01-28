# class类 python面向对象思想
class Student(object):
  def __init__(self,name,score):
    self.name = name
    self.score = score
  def get_score(self):
    if self.score >= 90:
      return 'A'
    elif self.score >= 60:
      return 'B'
    else:
      return 'C'
bart = Student("Bart Simpson",59)
print(bart.name)
print(bart.score)
print(bart.get_score())
lisa = Student('lisa',89)
print(lisa.get_score())
  