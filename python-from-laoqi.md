## 1 基本数据类型

1. 数字

* id() 返回在内存的地址

* type() 返回数据类型

2. 变量

* 对象有类型 变量无类型

对象类型也可以用type查看

3. python 不存在整数溢出问题

4. python 浮点数精度问题  

*  decimal模块  十进制高精度

*  fractions   有理数高精度

*  Numerical python 

4. 引入模块

```python
import module-name

from module1 import module11

```

5. 数学函数

%   求余   

divmod()   返回商和余

round()    四舍五入  

math模块  import math   

dir(module-name)   

help(function-name)

abs() 绝对值

6. tips

* 设置解释器  interpreter

```
#！/usr/bin/env python 
```

* 设置编码

```
#coding: utf-8 

# _*_ coding: utf-8 _*_
```

* 单行注释  #

* 多行注释  三个单引号 

* 语句与表达式区别：表达式就是某件事   语句是做某件事  

7. 字符串

* 单引号 双引号 包裹

* print()  输出字符

print的返回值默认是以\n结尾

* 双引号包裹单引号

* 转义符  \

* 连接字符  + 

* str()  将整数对象转换为字符串对象

* repr(object)  返回一个对象的 string 格式

* repr 和 `` 一样 没区别

* 原始字符串

用转义符能够让字符串中的某些符号表示原来的含义  
而不是被解析成某种具有特别能力的符号  

* raw_input() 2.0 input() 3.0

* 字符串可以通过索引访问字符

lang = 'study python'

print lang[0]  // s

print 'study python'[1] // t

string.index(char)  // return index  只会找到第一个字符的位置   

string[start:end]  不包含的end  

start 不写 默认是0   

end   不写 默认是长度    

如果start end 都不写 复制一份   

len()  返回长度  

\+ 连接两个字符串  

\* 重复字符  

in 判断元素是否存在于序列中  

max(str) 最大值   ascii值

min(str)  最小值   

cmp(str1, str2)  比较字符串是否相同   

ord(char)  返回ascii值   

chr(ascii值)  返回字符   

dir(str)  查看字符串的方法   

split(分隔符)  返回list   

strip  lstrip rstrip  去掉空格   

upper lower capitalize isupper islower istitle   

join  char.join(array)  以char连接数组

8. 字符串格式化

* %s      字符串 str()

* %r      字符串 repr()

* %c      单个字符

* %b      二进制

* %d      十进制数字

* %e      指数

* %f      浮点数

String.format(1,2)    
26.py


9. 字符编码

ascii码    8位   

unicode  万国码    

unicode的实现方式成为unicode转换方式 unicode transformation format  UTF   

utf-8 是一种针对unicode的可变长度字符编码  

10. encode decode 

python2默认编码是ascii 通过encode()可以将对象的编码转换为指定编码格式  

* import codecs  codecs.open(filename, encoding="utf8")


11. 列表 list

* 用[]表示一个list

* 值可以是任意类型

* bool(a)  a如果是空list 返回值false   


12. lsit 索引和切片

* [0]  从左边开始0  从右边开始-1

* [start:end] 

* index()  返回位置

* 序列的切片 一定要左边的数字小于右边的数字  

* 反转  [::-1]  reversed(list)

* reversed()  返回一个可迭代对象

可以将字符串返回一个反转的list   


* len()

* + 连接两个列表 

* \* 重复元素  [] * 3

* in 

* max  min 

* cmp()

* append(x)  list[len(list):] = x

* extend(itetatorObject)

* iterable iterator

* 如何判断一个类型是否可迭代

hasattr(obj, '__iter__')   

* count()  计算一个元素出现次数

* inert(i, x) 

* remove(x)

* pop(i)  默认是后一个

* list.reverse()  反转

* 
