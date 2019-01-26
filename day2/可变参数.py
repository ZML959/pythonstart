def calc(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum 

print(calc(1,2))
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
print(calc(*nums))
# *nums 表示把 nums这个list的所有元素作为可变成3参数传进去。

def person(name, age, **kw):
  print('name',name,'age',age,'other',kw)

person('Michael',30)
