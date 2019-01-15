# python 字典
d = {"key1":"123","key2":"234","key3":"345"}
print(d["key1"])
c=d.get("key4",'_1')
#.get 检查d里面是否存在key4值，如果key不存在 则返回规定的"_1"
c = "key4" in d
c = "key3" in d
print(c)
d.pop("key1")
print(d)
newSet = set([1,2,3,4,3,4,3])
print(newSet)
newSet.add(9)
newSet.remove(2)
print(newSet)
set1 = set([1,2])
set2 = set([2,3])
print(set1 & set2)
print(set1 | set2)
