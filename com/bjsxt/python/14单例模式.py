class Singleton:
    __instance=None
    __First_init=True

    def __init__(self,name):
        if self.__First_init:
            self.__First_init=False
            self.name=name
            print("init")

    def __new__(cls,name):
        print("new")
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
            pass
        return cls.__instance
    pass

    def run(self):
        print("running")

# 只能赋值一次
s=Singleton("zhangsan")
s1=Singleton("lisi")
print(id(s))
print(id(s1))
s1.run()
s.run()

print(s.name)
print(s1.name)