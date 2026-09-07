# Elements 项目开发规范

> 本规范基于项目实际代码风格提炼，覆盖目录职责、命名约定、import 规则、
> Scene 编写范式、配置约束与 git 工作流。新增代码请严格遵守。

---

## 一、目录结构与职责

```
Elements/
├── common/                  # 共享代码（所有命题均可复用）
│   ├── math_utils.py        # MathUtils 几何计算工具（唯一来源）
│   └── scenes.py            # Logo 动画函数、场景辅助函数
├── vol1_geometry/          # 第一卷 几何基础（对应《几何原本》Book I）
│   ├── proposition_1.py     # 命题 I.1
│   └── ...
├── vol2_geometry/          # （未来）第二卷
├── experiments/             # 学习 / 试验脚本（不纳入产品输出）
├── assets/logo/             # 静态资源占位
├── docs/notes.md            # 学习笔记
├── manim.cfg                # 全局唯一配置，不硬编码绝对路径
├── requirements.txt         # 依赖版本锁定
├── .gitignore               # 禁止 media/pyc/.idea 入库
├── README.md                # 项目说明
└── CONTRIBUTING.md          # 本规范
```

### 各目录职责边界

| 目录 | 放什么 | 不放什么 |
|------|--------|----------|
| `common/` | 跨命题复用的工具函数 / Logo 动画 | 具体命题逻辑、实验性代码 |
| `volX_*/` | 一卷内的命题 Scene | 工具类（放 common）、跨卷共享代码 |
| `experiments/` | Manim 学习脚本、临时试验、渲染原型 | 正式命题（放 volX_*） |

---

## 二、命名约定

### 2.1 文件名

| 类别 | 格式 | 示例 |
|------|------|------|
| 命题文件 | `proposition_<N>.py` | `proposition_1.py`、`proposition_12.py` |
| 工具模块 | `snake_case.py` | `math_utils.py`、`scenes.py` |
| 实验脚本 | 自由但有意义 | `SquareToCircle.py`、`2024_11_02.py` |

### 2.2 包名

全部小写 + 下划线：`common/`、`vol1_geometry/`、`experiments/`

### 2.3 类名

| 类别 | 格式 | 示例 |
|------|------|------|
| 命题 Scene | `Volume<卷号>Proposition<罗马数字>` | `VolumeIPropositionIV` |
| 工具类 | `PascalCase` | `MathUtils` |
| 实验 Scene | `PascalCase` 自由命名 | `SquareToCircle`、`Positioning` |

**命题 Scene 命名模板**：

```python
# 卷号用大写罗马数字（I / II / III / ...）
# 命题号用大写罗马数字（I / II / III / ...）
class VolumeIPropositionV(Scene):
    """第一卷 命题 V：xxx"""
```

### 2.4 函数 / 方法名

全部 `snake_case`：

- Logo / 场景辅助函数：`play_logo_animation()`、`play_rabbit_logo(scene)`
- 几何计算方法：`find_intersection_points()`、`find_line_circle_intersection()`
- Scene 内部方法：`show_proof()`、`move_scene_elements()`

### 2.5 变量名

- 坐标常量用大写：`A = np.array([-1, 0, 0])`、`ORIGIN`、`UP`、`LEFT`
- 图元变量用 `snake_case` + 可读缩写：`line_AB`、`dot_C`、`circle1`、`text_2`
- Manim 颜色/位置常量直接用 Manim 命名：`BLUE`、`YELLOW`、`GREEN`、`UP`、`RIGHT`

---

## 三、Import 规范

### 3.1 Manim：星号导入

统一使用 `from manim import *`，Manim 图元/颜色/动画函数均可直接用：

```python
# ✅ 正确
from manim import *

# ❌ 不要：显式列出所有导入
from manim import Scene, Circle, Dot, Line, VGroup, ...   # 太长

# ❌ 不要：显式列出星号已覆盖的导入（冗余）
from manim import *
from manim import Dot, Line                               # 星号已包含
```

### 3.2 common 模块：显式导入

从 `common/` 导入时**不能**用星号，必须显式写导入名：

```python
# ✅ 正确
from common.math_utils import MathUtils
from common.scenes import play_logo_animation, play_rabbit_logo

# ❌ 不要
from common.math_utils import *
from common.scenes import *
```

### 3.3 numpy：习惯用法

```python
import numpy as np
```

### 3.4 禁止相对导入

```python
# ❌ 不要
from .math_utils import MathUtils
from ..common.scenes import play_logo_animation

# ✅ 一律用绝对导入（以项目根为起点）
from common.math_utils import MathUtils
```

### 3.5 完整 import 区块模板

命题文件的 import 区块应长这样：

```python
from manim import *          # Manim 图元/动画
import numpy as np          # 数值计算
from common.math_utils import MathUtils       # 几何计算工具
from common.scenes import play_logo_animation # Logo 动画
```

---

## 四、Scene 编写范式

### 4.1 基本骨架

```python
from manim import *
import numpy as np
from common.math_utils import MathUtils
from common.scenes import play_logo_animation


class VolumeIPropositionX(Scene):
    """第一卷 命题 X：命题陈述一句话。"""

    def construct(self):
        # 1) Logo 动画（每个命题视频开头必加）
        play_logo_animation(self)

        # 2) 标题 / 命题陈述
        # 3) 几何作图（点、线、圆、多边形）
        # 4) 证明过程（show_proof 方法）
        # 5) 收尾

    def show_proof(self) -> object:
        """推理文本动画。因依赖 self.play，保留为 Scene 内部方法。"""
        ...
```

### 4.2 Logo 调用

每个命题 `construct()` 的**第一行**必须是 logo 动画之一：

```python
# 方式 A：项目默认 logo（《几何原本》+ YOHO）
play_logo_animation(self)

# 方式 B：兔子 logo
play_rabbit_logo(self)
```

**禁止**在命题场景内自行实现 LogoScene 或复制粘贴旧版本。

### 4.3 MathUtils 调用

几何计算必须通过 `MathUtils` 类的静态方法，**禁止**在命题文件内重新定义 `find_intersection_points` / `find_line_circle_intersection` 等工具方法：

```python
# ✅ 正确
intersection_points = MathUtils.find_intersection_points(A, B, line_AB.get_length())
intersection_with_BF = MathUtils.find_line_circle_intersection(B, extended_dot_F, B, line_BC.get_length())

# ❌ 不要：在 Scene 内重复定义同名静态方法
class VolumeIPropositionII(Scene):
    @staticmethod
    def find_intersection_points(A, B, r):   # 重复了！
        ...
```

### 4.4 show_proof 的归属

`show_proof()` / `show_proof_texts()` 这类**依赖 `self.play` 方法**的动画辅助函数，保留为 Scene 的内部实例方法，不抽到 `common/`。

### 4.5 construct 方法内的代码组织顺序

推荐顺序：

1. `play_logo_animation(self)` —— logo
2. 标题 / 命题陈述文本
3. 几何体（点 → 线 → 圆 → 多边形）
4. 证明文本 / `show_proof()`
5. 清理 / FadeOut

### 4.6 颜色使用约定

| 颜色 | 用途 |
|------|------|
| `BLUE` | 基准线 / 几何关系强调 |
| `GREEN` | 构造圆 / 辅助对象 |
| `YELLOW` | 圆 / 构造动画 |
| `RED` | 重点线段 / 结论高亮 |
| `BLACK` | 轮廓描边 |
| `WHITE` | 背景填充 / 反色 |
| `PINK` | 可爱元素（兔子鼻子、耳朵内部） |

---

## 五、manim.cfg 配置规范

### 5.1 唯一性

项目根目录的 `manim.cfg` 是**唯一**配置文件，不允许在子目录再创建 `manim.cfg`。

### 5.2 可移植性

**禁止**在 `manim.cfg` 中写入硬编码绝对路径，必须注释掉：

```ini
# ❌ 不要
[ffmpeg]
ffmpeg_executable = D:\ProgramFiles\ffmpeg\bin

[latex]
path = D:\soft\texlive\2024\bin\windows\pdflatex.exe

# ✅ 正确（注释掉，依赖系统 PATH）
[ffmpeg]
# ffmpeg_executable = D:\ProgramFiles\ffmpeg\bin

[latex]
# path = D:\soft\texlive\2024\bin\windows\pdflatex.exe
```

如需指定本机路径，取消注释并填入，但**不要提交带本机路径的 manim.cfg**。

### 5.3 常用配置项

| 配置 | 建议值 | 说明 |
|------|--------|------|
| `renderer` | `cairo` | 默认矢量渲染器 |
| `frame_rate` | `60` | 帧率 |
| `pixel_height/width` | `1080 / 1920` | 16:9 输出分辨率 |
| `media_dir` | `./media` | 媒体产物目录（已被 .gitignore 忽略） |
| `background_color` | `BLACK` | 默认黑底 |

---

## 六、代码风格与注释

### 6.1 行宽

每行不超过 100 字符（manim 链式调用允许适度超宽，但尽量换行）。

### 6.2 链式调用换行

Manim 图元初始化 + 链式 `.rotate().move_to().set_fill()` 建议每行一个方法：

```python
# ✅ 推荐：每行一个链式方法
ear_left = Ellipse(width=0.45, height=1.15, color=BLACK) \
    .rotate(20 * DEGREES) \
    .move_to(LEFT * 0.55 + UP * 1.8)

# 也可以用括号包裹（PEP 8 风格）
ear_left = (Ellipse(width=0.45, height=1.15, color=BLACK)
    .rotate(20 * DEGREES)
    .move_to(LEFT * 0.55 + UP * 1.8))
```

### 6.3 中文注释

本项目注释可以用**中文**，但：

- 类 docstring 用中文一句话描述命题内容
- 关键变量 / 动画步骤可加中文注释解释意图
- `show_proof` 中的推理文本是动画对白，直接写中文

```python
class VolumeIPropositionIII(Scene):
    """第一卷 命题 III：给定两条不等线段，可在较长线段上截取一条等于较短线段。"""

    def construct(self):
        play_logo_animation(self)

        # 创建较长的线段 AB
        A = np.array([0, 0, 0])
        B = np.array([3, 0, 0])

        # 推理文本（动画对白）
        text_4 = Text('在A上取AE等于c,又以A为圆心、以AC为半径画圆ACE', font_size=25)
```

### 6.4 文件顶部 docstring

每个命题文件顶部建议加 docstring，说明命题内容与合并来源（若为合并文件）：

```python
"""
Proposition I.3: 给定两条不等线段，可在较长的线段上切取一条线段等于较短的线段。

合并自 _geo/vol1/PropositionI_3.py（基准）与 _2024 版。
保留基准版的 WZ 线段演示与扩展证明文本。
"""
```

### 6.5 删除代码与 TODO

- 旧代码**直接删除**，不要注释掉留着
- 未实现的动画 / 功能用 `# TODO:` 标记，不要用注释掉的代码占位

```python
# ✅ 正确
# TODO: 在线段 AP 消失前加上以 AP 为半径的圆，并进行说明

# ❌ 不要
# self.play(FadeOut(dot_P), FadeOut(line_AP), FadeOut(label_P))
# self.wait(6)
# 这里应该做 XX 但还没写
# video11 = VolumeIPropositionII()
# video11.construct()
```

---

## 七、Git 工作流

### 7.1 .gitignore 约束

以下内容**禁止**提交到 git：

```
__pycache__/
*.pyc
media/              # manim 生成的 mp4/svg/tex/partial_movie
*.mp4
*.svg
*.tex
.idea/              # PyCharm 配置
.vscode/            # VS Code 配置
```

### 7.2 提交前自检

每次 commit 前请确认：

- [ ] `manim.cfg` 未包含本机硬编码绝对路径
- [ ] 没有 `media/`、`__pycache__/`、`.idea/` 被误提交
- [ ] 新代码已通过 `python -m py_compile` 语法检查
- [ ] Logo 动画走的是 `play_logo_animation(self)` 或 `play_rabbit_logo(self)`，而非自造 LogoScene

### 7.3 提交信息格式

```
<类型>: <简短描述>

可选：详细说明

类型：feat / fix / refactor / docs / chore
```

示例：

```
feat: 添加命题 I.5 的 VolumeIPropositionV 场景

fix: 修复 show_proof 中 all_texts 未定义导致的 FadeOut 报错

refactor: 将 PropositionI_3 两版合并，以 _geo 版为基准

docs: 更新 CONTRIBUTING.md 代码规范
```

---

## 八、新增命题 Checklist

新增一条命题时，按以下步骤操作：

1. 在 `volX_*/` 下创建 `proposition_<N>.py`
2. 场景类命名 `Volume<卷号>Proposition<罗马数字>`
3. `construct()` 开头第一行调用 `play_logo_animation(self)`
4. 几何计算走 `MathUtils.find_intersection_points` / `MathUtils.find_line_circle_intersection`
5. 推理文本动画封装为 `show_proof(self)` 方法
6. 文件顶部加 docstring 说明命题内容
7. 提交前确认 `.gitignore` 未被绕过

---

## 九、快速参考

### 常用 Import 模板

```python
from manim import *
import numpy as np
from common.math_utils import MathUtils
from common.scenes import play_logo_animation       # 或 play_rabbit_logo
```

### 常用 MathUtils 调用

```python
MathUtils.find_intersection_points(A, B, r)                 # 两等圆交点
MathUtils.find_line_circle_intersection(A, B, C, radius)    # 线段与圆的交点
```

### 渲染命令

```bash
manim -pql vol1_geometry/proposition_4.py VolumeIPropositionIV    # 低质量预览
manim -pqh vol1_geometry/proposition_4.py VolumeIPropositionIV     # 高质量输出
```

---

> 本规范随项目演进迭代，修改时同步更新 REFACTOR_PLAN.md 中的规范相关章节。
