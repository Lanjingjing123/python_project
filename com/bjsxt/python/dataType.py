# number 类型
a = 111
print(isinstance(a,int))
print(a)

print('==================================')
# String 类型

str = 'Runoob'
print(str)
print(str[0:-2])

# list
lists =['abcd', 387, 234.243, 'hkjh']
print("===================")
for i in lists:
    print(i)

# tinylistssf = [123, 'runoob']
# print(lists)
# print(lists[1:3])
# list[2:3] = [4, 5]



# print(list+tinylistssf)

# tuple
# tuple1 = ('add', 786, 2.23, 'runoob', 30.2)
# print(tuple1)

print("-----------------------")
a = '123'
b = '456'
c = '789'
str1 = '{_a},{_b},{_c}'
str =  str1.format(_a=a,_b=b,_c=c)
print(str)