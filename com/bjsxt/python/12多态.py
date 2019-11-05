class F1(object):
    def show(self):
        print("F1 show ...")
        pass
    pass

class S1(F1):
    def show(self):
        print("S1 show ...")
        pass
    pass

class S2(F1):
    def show(self):
        print("S2 show ...")
        pass
    pass

class S3:
    def show(self):
        print("S3 show...")

def Func(obj):
    obj.show()
    pass


s1=S1()
s2=S2()
f1 =F1()
s3=S3()

Func(s1)
Func(s2)
Func(f1)
Func(s3)