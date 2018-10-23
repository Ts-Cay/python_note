# Python 笔记
****

#### 内建函数 BIF

    - locals() : 显示所有的局部变量
    - globals() : 显示所有的全局变量
    
    - eval(string,globals=None,locals=None) : 把一个字符串当作表达式来执行
    - exec() : 功能类似,但是没有返回结果
     

#### 字符串常用方法
   - 判断字符串内容的常用方法：
      - isalnum()  : 字符串只包含数字和大小写字母
      - isalpha()  : 字符串只包含 大小写字母组成
      - isdigit()  : 字符串只包含数字
      - islower()  : 字符串只包含小写字母
      - isupper()  : 字符串只包含大写字母
      - istitle()  : 字符串的首字母只要是大写就可以
      - isspance() : 字符串都是空白字符


#### 列表推导式
     """
         li = [1,2,3,4,"aaa","AAA"]
         li2 = [k.lower() for k in li if str(k).isupper()]
     """
    
---

##### lambda 函数
    格式为：
        lambda x,y : x+y
    
##### if 表达式
    格式为：
        x if 表达式 else y
        当表达式成立(Ture)时返回x 否则返回 y
        
## OOP

### 对象与类
     stu = Student()
     stu叫做实例对象,Student叫做类对象
     
     当对实例对象的成员操作时,操作的是实例对象的成员,并不影响类对象的成员
     若实例对象中没有这个成员时,会使用类对象的成员
     对实例对象的成员修改不会影响类对象的成员.
     
     init方法中的self就是将实例对象与类对象进行绑定
     同时可以为实例对象绑定 成员
     
     self 代表的是 实例对象
     
     相当于：
        JAVA在创建对象时new出来的一个对象,对这个对象的成员赋值或修改
        并不影响类中的成员
        并且可以通过反射机制动态的为对象添加或删除成员或方法
        JAVA封装：
                属性私有化
                行为公开化
        JAVA中 父类引用指向子类对象时：
                1. 能点出来什么方法的看引用
                2. 点出来的方法是什么看对象
     
     __dict__:查看实例对象或类对象的成员
     
---

    类与对象的相关BIF:
        - issubclass(class A,classinfo B) : 判断A是否是B的子类
        - isinstance(object A,classinfo B) : 判断对象a是否是B的实例对象
    
    实例对象属性相关BIF：
        - hasattr(object,name) : 判断对象是否有指定的属性
        - getattr(object,name[,default]) : 返回对象指定的属性值,若不存在,返回default的值,若未设置值,抛出AttributeError异常
        - setattr(object,name,value) : 设置对象中指定的值,若不存在,则为实例对象新建属性并赋值
        - delattr(object) : 删除对象中指定属性,若不存在,则抛出AttrbuteError异常 
    
    类中通过属性设置属性的方法：
    
        property(fget=None,fset=None,fdel=None,doc=None)
            fget : 成员的get方法名
            fset : 成员的set方法名
            fdel : 成员的del方法名
            
        x = property(getX,setX,delX)
        
  
        
        
        
        
### 魔法方法：

     常用方法：
   
        '''
         __str__  : 打印类的信息 
         __repr__ : 返回的字符串可以使用 eavl()方法使用
        
        一般用法为: __repr__ = __str__
        
         __getattr__   : 
         __setattr__   :
         __delattr__   :
         __getattrbute__ :
   
        '''


