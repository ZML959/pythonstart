class Animal(object):
  def run(self):
    print('Animal is running...')

class Dog(Animal):
  def eat(self):
    print('Dog is eating...')

class Cat(Animal):
  def run(self):
    print('cat is runing...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print(isinstance(dog,Animal))

#定义的函数可以传入实例，到时候就能传进来
def run_twice(animal):
  animal.run()
  animal.run()

run_twice(cat)