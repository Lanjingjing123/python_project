class Person(object):
    name="zhangsan"
    __age=30
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        pass

    # 类方法用注解，外部不能改变类方法中的初始化参数
    # @classmethod
    # def getAge(clz):
    #     return clz.__age
    # pass

    # 静态类方法注解，可以为空参，与 @classmethod效果一样
    @staticmethod
    def getAge():
        return Person.__age

    def getAge2(self):
        return self.__age

print(Person.name)
# print(Person.getAge(50))


p=Person("lisi",100)
Person.name="wangwu"
print(p.name) # lisi
print(p.getAge()) # 100
print(p.getAge2()) # 30
print(Person.name) # wangwu