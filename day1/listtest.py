L=[
  ['apple','banana','orange'],
  ['java','python','javascript','php'],
  ['name','age','school']
]
print(L[0][0])

age = 3
if age>3:
  age = 18
elif age == 3:
  age = 3
else:
  age = 0

print(age)

# 小明身高1.75 体重80.5kg,请根据BMI公式
# 低于18.5：过轻
# 18.5-25：正常
# 25-28:过重
# 28-32:肥胖
# 高于32:严重肥胖
# 体重除以身高的平方
height = 1.75
weight = 75
BMI = weight/(height*height)
# print(BMI)
if BMI<18.5:
  print('过轻')
elif 18.5<=BMI<25:
  print('正常')
elif 25<=BMI<28:
  print('肥胖')
elif 28<=BMI<32:
  print('严重肥胖')
  
