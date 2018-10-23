
# 测试类与对象相关的BIF
class A():
    pass

class B(A):
    pass

class C():
    pass


def fun():
    a = A()
    b = B()
    c = C()


    # 判断 B 是否是 A 的子类
    #print(issubclass(B,A))
    # 判断 C 是否是 A 的子类
    #print(issubclass(C,A))

    # 判断a是否是A的实例对象
    #print(isinstance(a,A))
    # 判断b是否是A的实例对象
    #print(isinstance(b,A))
    # 判断c是否是A的实例对象
    #print(isinstance(c,A))

    A.x = 6

    attr = getattr(a,"x")
    print(attr)

class A():
    y = 6
    x = 1
    def __init__(self,x=5):
        self.x = x

def fun2():
    a = A()
    a.y = 10
    a.x = 20
    print("a.y={0} \na.x={1} \n\nA.y={2} \n".format(a.y,a.x,A.y))

    print("*" * 20)

    # A.x = 200
    # A.y = 300

    print("a.y={0} \na.x={1} \nA.x={3}\nA.y={2} \n".format(a.y, a.x, A.y,A.x))
    print("*" * 20)

    c = A()

    print("c.y={0} \nc.x={1} \nA.x={3}\nA.y={2} \n".format(c.y, c.x, A.y, A.x))
    """
    c.x=5是因为
        A.x 是 A的成员变量是属于类的成员属于A的
        而在c创建时,通过调用__init__(self,x=5)方法 将c当作参数传入了self中,所以 init方法中
        就变成了
        c.x = x , 所以c.x是属于实例对象c 而不是属于类对象A的
        如果实例对象没有 x 这个成员 则会查找 类对象中的成员
        就像是 c.y = 300
        其中c.y 指向的就是 类对象A中的成员y
        成员的检查规则是：
        先检查 实例对象,若实例对象存在成员对象 则调用实例
    """
if __name__ == '__main__':
    fun2()



