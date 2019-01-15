#for in 循环  循环list 或 tuple中
names = ['Michael','Bob','Tracy']
for name in names:
  print(name)
# for x in 
sum = 0
for x in [1,2,3,4,5,6,7,8]:
  sum += x
print(sum)

n = 1
while n <= 100:
  print(n)
  n+=1
print('end')

while n <= 100:
  if n > 10 :
    break
  print(n)
  n+=1
print('END')