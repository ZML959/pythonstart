# 类里面的私有属性 
class Student(object):
  def __init__(self, name, score):
    self.__name = name  #__变量名称前面加以后变成私有属性，方法外面的东西无法去访问
    self.__score = score
  def get_data(self):
    print('%s:%s'%(self.__name,self.__score))
  def get_name(self):
    print(self.__name)
  def get_score(self):
    print(self.__score)
    if self.__score <= 60:
      print('C')
    elif self.__score >60 and self.__score <=80:
      print('B')
    else:
      print('A')
  def set_score(self,score):    #设置class里面的不可变私有属性
    self.__score = score
    self.get_score()

lisa = Student('lisa',80)
# print(lisa.__name)
# lisa.get_score()
# lisa.get_name()
# lisa.get_data()
# lisa.set_score(66)
lisa.set_score(90)