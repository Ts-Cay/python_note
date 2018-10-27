# Python 笔记
****

#### 内建函数 BIF

    - locals() : 显示所有的局部变量
    - globals() : 显示所有的全局变量
    
    - eval(string,globals=None,locals=None) : 把一个字符串当作表达式来执行
    - exec() : 功能类似,但是没有返回结果
     
---
#### 字符串常用方法
   - 判断字符串内容的常用方法：
      - isalnum()  : 字符串只包含数字和大小写字母
      - isalpha()  : 字符串只包含 大小写字母组成
      - isdigit()  : 字符串只包含数字
      - islower()  : 字符串只包含小写字母
      - isupper()  : 字符串只包含大写字母
      - istitle()  : 字符串的首字母只要是大写就可以
      - isspance() : 字符串都是空白字符

---
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

---
## OOP

### 对象与类

*关于Python中类对象和实力对象理解引用自[理解类对象,实例对象](https://www.cnblogs.com/wf-skylark/p/9009770.html)*
      
     dog = Animal()
     其中：
            dog   --  实例对象
            Animal -- 类对象
    
     类属性：
        类对象拥有的属性,类对象和实例对象均可以访问
        被它们共同所有
     
     公有类属性：
        相当于JAVA被public修饰的属性
        
     私有类属性:
        相当于JAVA中被private修饰的属性
        不能被直接调用,需要通过方法来调用
        在python中私有属性使用'__变量名'来定义私有属性
        
     关于公有类属性：
        公有类属性被实例对象引用时,相当于实例对象(dog)在实例方法中创建了一个
        和类属性名字相同的变量,此时和类属性没有一点关系
     
        当对实例对象的属性操作时,操作的是实例对象的属性,并不影响类对象的属性
        (相当于实例对象会自己创建一个局部变量,只是变量名与类属性的名字相同)
        若实例对象中没有这个属性时,会使用类对象的属性
        对实例对象的属性修改不会影响类对象的属性.
        (其中 方法也是属性)
     
     类方法: 
        `
        @classmethod
        def run(cls):
            pass
        `
        类方法的第一个参数必须为类对象,一般用cls表示,通过cls引用的必须是类属性
        和类方法
        
     静态方法：
        `
        @staticmethod
        def msg():     #定义时可以没有参数
            pass
        `
        静态方法不需要类和对象参与.

          
     init方法中的self就是将实例对象与类对象进行绑定
     同时可以为 实例对象绑定属性
     
     self 代表的是 实例对象
     
     相当于：
        JAVA在创建对象时new出来的一个对象,对这个对象的成员赋值或修改
        并不影响类中的成员的值
        
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
---         
### 魔法方法：
    - 打印类的信息的魔法方法:
        `
          __str__  : 打印类的信息 
          __repr__ : 返回的字符串可以使用 eavl()方法使用
        `
   一般用法为: __repr__ = __str__
   
    - 类的属性的魔法方法: 
        `
         __getattr__   : 
         __setattr__   :
         __delattr__   :
         __getattrbute__ :
        `


