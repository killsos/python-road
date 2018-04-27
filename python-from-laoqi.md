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
```

* 单行注释  #

* 多行注释  三个单引号 

* 语句与表达式区别：表达式就是某件事   语句是做某件事  

7. 字符串

* 单引号 双引号 包裹

* print()  输出字符

* 双引号包裹单引号

* 转义符  \

* 连接字符  + 

* str()  将整数对象转换为字符串对象

* repr(object)  返回一个对象的 string 格式
