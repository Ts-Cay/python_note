#Python 笔记
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
     
     当对实例对象的成员操作时,会引用实例对象的成员,
     若实例对象中没有这个成员时,会查看类对象的成员
     对实例对象的成员修改不会影响类对象的成员.
     
     相当于：
        JAVA在创建对象时new出来的一个对象,对这个对象的成员赋值或修改
        并不影响类中的成员
        并且可以通过反射机制动态的为对象添加或删除成员或方法
     
     __dict__:查看实例对象或类对象的成员
     
---

    类与对象的相关BIF:
        - issubclass(class A,classinfo B) : 判断A是否是B的子类
        - isinstance(object A,classinfo B) : 判断A是否是B的实例对象
        
### 魔法方法：

   - 常用方法：
   
        '''
        - __str __  : 打印类的信息 
        - __repr __ : 返回的字符串可以使用 eavl()方法使用
        
        一般用法为: __repr __ = __str __
        
        - __getattr __   : 
        - __setattr __   :
        - __delattr __   :
        - __getattrbute __ :
   
        '''


