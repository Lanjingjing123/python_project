class Animal(object):
    def __init__(self,name):
        self.name=name
    def run(self):
        print(self.name+"is running")
class Active(object):
    def active(self):
        print("active ...")

class Cat(Animal,Active):
    def __init__(self,name,type):
        super().__init__(name)
        # self.name=name
        self.type=type


cat=Cat("lele","cat")
cat.active()
cat.run();


'''
    多继承,继承方法有重复有顺序
'''
class A(object):
    def show(self):
        print("show A ...")

class B(object):
    def show(self):
        print("show B ...")

class C(A,B):
    pass

# class C(B,A)
#     pass
c=C()
c.show()
print(C.__mro__)