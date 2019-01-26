#-*- coding:utf-8 -*-
def my_first(x):
  if x >= 0:
    return x
    print('我大于0')
  else:
    return -x
    print('我是小于0')

print(my_first(-99))
#- - 
def power(x):
  return x * x
a = power
print(a(99))


def power1(x,n):
  s = 1
  while n > 0:
    n = n - 1 
    s = s * x
  return s
print(power1(10,8))

# def add_end(L=[]):
#   L.append('END')
#   return L

def add_end(L=None):
  if L is None:
    L = []
  L.append('END')
  return L

print(add_end([1,2,3]))
print(add_end([1,2,3]))
print(add_end())
print(add_end())


