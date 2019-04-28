from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
    print(x)

# 访问元素
print (array1[0])
print (array1[2])
# 插入
array1.insert(1,60)
for x in array1:
    print(x)
# 删除
array1.remove(40)
# 查找
print (array1.index(30))
# 更新
array1[2] = 80


#List
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5,6,7]
list3 = ["a", "b", "c", "d"]
##访问元素
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list1[2] = 2001##更新元素
list1.append(2)##追加元素
del list1[2]##删除元素
len(list1)# 长度
[1,2,3] + [4,5,6] #合并
['a']*4 #重复


##set
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
print(Days)
##不能访问一个特定的元素，只能访问整个集合
for d in Days:
	print(d)

Days.add("Sun") # 添加元素
Days.discard("Sun") #删除元素
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB #交集
AllDays = DaysA & DaysB #并集
AllDays = DaysA - DaysB # 在A里但不在B里
SubsetRes = DaysA <= DaysB # A是否是B的子集
SupersetRes = DaysB >= DaysA
 


#Tuple
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print("tup1[0]: ", tup1[0]);
print("tup2[1:5]: ", tup2[1:5]);
##不能更新，只能重新构造。 不能删除特定元素， 只能整个删除
tup3 = tup1 + tup2;
print(tup3);
del tup1


##dict
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
dict['Age'] = 8; # 更新
dict['School'] = "DPS School"; # 添加新的
del dict['Name']; # 删除键为'Name'的键值
dict.clear();     # 删除字典所有元素
del dict ;        # 删除字典

##maps
import collections
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}
res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
##如果有重复的key， 选择最先出现的那个
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
# 打印所有的结果
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# 查看元素是否在字典里
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))

##更新maps
res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
dict2['day4'] = 'Fri'
print(res.maps,'\n')

## 2-D Array
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
print(T[0])
print(T[1][2])
T.insert(2, [0,5,11,13,6]) #插入
T[2] = [11,9] ##更新
T[0][3] = 7
del T[3] #删除

## Matrix
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)
# Print data for Wednesday
print(m[2])
# Print data for friday evening
print(m[4][3])

m_r = append(m,[['Avg',12,15,13,11]],0) #添加一行
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1) #添加一列
m = delete(m,[2],0) # 删除第3行
m = delete(m,s_[2],1) # 删除第3列
m[3] = ['Thu',0,0,0,0] #更新第四行



