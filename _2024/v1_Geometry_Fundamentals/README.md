"""
This file is used to define the functions used in the Geometry Fundamentals module.
该文件用于定义几何学基础模块中使用的函数。
"""

"""
python文件夹的注释在这里写
"""

"""
-- day09 --
读取文件时，判断路径是否存在？
import os
if os.path.exists(path):
    with open(path, 'r') as f:
        content = f.read()

使用with文件上下文管理器，可以自动关闭文件，避免忘记关闭造成资源泄露。
with支持同时对多个文件的上下文管理，如：
with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    f2.write(f1.read())

写入文本文件?
with open(path, 'w') as f:
    f.write(content)

-- day10 --
函数参数：
- 形参：形式参数，函数定义时的参数。
- 实参：执行函数传值时，传入的实际值。
- 实参的传递方式：
    - 位置参数：按照函数定义时的顺序，依次传入。
    - 关键字参数：通过参数名传入，可以不按顺序传入。
    - 默认参数：如果没有传入实参，则使用默认值。
    - 动态参数：可以传入任意数量的参数，但必须在参数列表的最后。
    - 关键字参数：可以传入任意数量的关键字参数，但必须在参数列表的最后。
- 位置参数 
- 默认参数：默认参数必须位于必选参数之后。
- 动态参数：*args，可以传入任意数量的参数，但必须在参数列表的最后。元组形式。
- 关键字参数：**kwargs，可以传入任意数量的关键字参数，但必须在参数列表的最后。字典类型接收参数

动态参数和关键字参数的使用：
def func(*args, **kwargs):
    print(args)
    print(kwargs)
既能接收位置参数，又能接收关键字参数。
- 位置参数：func(1, 2, 3),元组形式。
- 关键字参数：func(a=1, b=2)，字典形式。
- 位置参数和关键字参数混合：func(1, 2, 3, a=1, b=2)
- 动态参数func(1, 2, 3, a=1, b=2)

-- day11 --

"""

