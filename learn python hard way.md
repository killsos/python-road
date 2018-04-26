# 笨方法学python笔记

### 1

1. 退出python ctrl + d

2. 注释  #


3. 文件格式

```python

# -*- coding: utf-8 -*-

```

4. 数字和数学计算

```python
+ - * / %  

> < >= <=

```

5. 变量和命名

变量 variable   

6. 格式化字符串 format string

%d %s %r   

%r 用来调试最好   

7. 换行符 new line

\\n

8. 转义序列 escape sequences

9. 输入 raw_input("提示字符")

10. input 输入的字符会被当代码

11. pydoc 查询函数功能

12. argv  argument variable  参数变量

13. 模块 module

14. 库 library

15. prompt   >

16. open  返回 fileObject

17. 读写文件

* open()   返回file object

* read()   返回file content

* readline() 返回file中一行

* truncate()  清空文件内容

* write(stuff)  将stuff写入文件

* close()  关闭文件

如果想向文件写内容 需要open加写权限  
write read append   

18. 函数  变量  代码

def functionName(*args):
  code

剩余参数 *args

函数名 变量名 规则：只要以字母 数字 以及下划线组成 但不能以数字开头   

\* 剩余参数   

19. seek()

```python

fileobject.seek(0)
# seek函数的处理对象是字节而非行

readline里边的代码会扫描文件的每一个字节  
直到找到一个\n为止
然后它停止读取文件
```

20. 函数的返回值

return  如果没写 返回值None   

21. 字符串处理库 ex25

22. 逻辑关系

and  or  not  !=   ==  >= <= True False   

!= 是主流用法  <> 也是不等于 逐步废弃   

23. if

```python
if logic:

if logic:
  code
elif logic:
  code
else:
  code
```

24. 数组

[]  

append()  添加   

array[index]

虚数 ordinal number

基数  cardianl number

25. for

```python

for i in array

```

26. range 

range(0, 10) 0-9 10不包含

27. while

while logic:
  code

28. 中断

```python
form sys import exit

exit(0)  正常退出

exit(1)  错误退出
```

29. 字典 dictionary  dicts dict

30. 面向对象语言 oop

class __init__(self)   

* self 在类的函数中 self指代被访问的对象或者实例的一个变量  

* 继承 inheritance 指一个类可以继承另一个类的特性 和父子关系类似

* 组合 composition 指一个类可以将别的类作为它的部件构建起来 

* 属性 attribute 类的一个属性 来自于组合

* is-a 描述继承关系 

* has-a 描述组合关系


















