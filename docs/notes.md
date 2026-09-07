# 学习笔记

> 本文档汇集项目开发过程中积累的 Python / Manim / LaTeX 学习笔记，
> 与项目主文档（README.md）分离，便于查阅。

---

## 一、Manim 执行命令

执行命令示例：`manim -p -ql first.py SquareToCircle`

执行时如果出现权限相关的问题，把电脑的安全软件关一下。

### 命令选项说明

> `manim -p -ql first.py SquareToCircle` ：运行 `first.py` 文件中的 `SquareToCircle` 类

- `-p` ：表示渲染完毕后自动预览动画
- `-ql` ：低质量（quality low）渲染，速度快但画质一般；480p 分辨率
- `-qm` ：中质量（quality medium）渲染，速度与画质适中
- `-qh` ：高质量（quality high）渲染，速度慢但画质好；720p 分辨率
- `first.py` ：具体文件名
- `class_name` ：具体命题（场景类）名称

### 手动指定分辨率

```
manim -p -r 1920,1080 test_2.py SquareToCircle     # 1080p
manim -p -r 3840,2160 test_2.py SquareToCircle     # 4K
```

### 手动指定帧率

```
manim -p -ql -r 1920,1080 --fps 60 test_2.py SquareToCircle
```

`--fps 60` 即每秒 60 帧，默认是 15 帧（15fps）。

---

## 二、LaTeX 安装与排错

1. 安装 latex：https://blog.csdn.net/Nicolecocol/article/details/136968456
2. 注意 `manim.cfg` 文件中 latex 的路径是否正确
3. 若执行时出现 `RuntimeError: latex failed but did not produce a log file. Check your LaTeX installation.` 的错误，可执行以下命令：

```
cd C:\Users\xxxx\.texlive2024\texmf-var\web2c\pdftex
fmtutil --all --force         # 重新生成格式文件
```

---

## 三、Python 基础笔记（day09 ~ day11）

### day09：文件读写

读取文件时，判断路径是否存在？

```python
import os
if os.path.exists(path):
    with open(path, 'r') as f:
        content = f.read()
```

使用 `with` 文件上下文管理器，可以自动关闭文件，避免忘记关闭造成资源泄露。
`with` 支持同时对多个文件的上下文管理，如：

```python
with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    f2.write(f1.read())
```

写入文本文件：

```python
with open(path, 'w') as f:
    f.write(content)
```

### day10：函数参数

- **形参**：形式参数，函数定义时的参数。
- **实参**：执行函数传值时，传入的实际值。

实参的传递方式：

- 位置参数：按照函数定义时的顺序，依次传入。
- 关键字参数：通过参数名传入，可以不按顺序传入。
- 默认参数：如果没有传入实参，则使用默认值。
- 动态参数：可以传入任意数量的参数，但必须在参数列表的最后。
- 关键字参数：可以传入任意数量的关键字参数，但必须在参数列表的最后。

要点：

- 位置参数
- 默认参数：默认参数必须位于必选参数之后。
- 动态参数：`*args`，可以传入任意数量的参数，但必须在参数列表的最后。元组形式。
- 关键字参数：`**kwargs`，可以传入任意数量的关键字参数，但必须在参数列表的最后。字典类型接收参数。

动态参数和关键字参数的使用：

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

既能接收位置参数，又能接收关键字参数。

- 位置参数：`func(1, 2, 3)`，元组形式。
- 关键字参数：`func(a=1, b=2)`，字典形式。
- 位置参数和关键字参数混合：`func(1, 2, 3, a=1, b=2)`
- 动态参数：`func(1, 2, 3, a=1, b=2)`

### day11：静态方法

什么是静态方法？如何使用？

`@staticmethod` 是一个装饰器，用来定义静态方法。不需要 `self` 参数，可以直接通过类名调用。
只依赖传入的参数，不依赖于实例的状态。

1. 可直接被调用，不需要实例化对象：如 `math.sqrt(x)`

本项目中的 `MathUtils` 类的 `distance` / `find_intersection_points` / `find_line_circle_intersection`
均为静态方法，可通过 `MathUtils.find_intersection_points(...)` 直接调用。
