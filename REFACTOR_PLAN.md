# Euclid 项目结构整改方案

> 本文档记录项目结构评估结论与分阶段整改方案，作为本次重构的操作手册。

---

## 一、现状概览

**Git 跟踪文件统计（共 1492 个）：**

| 类别             | 数量   | 占比    | 说明                                |
| ---------------- | ------ | ------- | ----------------------------------- |
| 媒体产物         | 1455   | 97.5%   | mp4 / svg / tex / partial_movie 等 |
| `.idea` IDE 配置 | 8      | 0.5%    |                                     |
| `__pycache__/.pyc`| 6      | 0.4%    |                                     |
| Python 源码      | 18     | 1.2%    | 实际有效代码                        |
| 配置 / 文档      | 5      | 0.3%    |                                     |

**核心矛盾**：18 个源码文件被 1455 个生成产物淹没。

---

## 二、问题清单（按严重程度）

### 🔴 严重问题

#### P1. 无 `.gitignore`，媒体产物与缓存被提交
- 1455 个媒体文件（mp4/svg/tex）混入版本库
- 6 个 `__pycache__/*.pyc` 缓存被跟踪
- `.idea/` IDE 配置整体入库

#### P2. 严重的代码重复
- `utils.py` 两份几乎逐字相同（`_2024/v1_Geometry_Fundamentals/utils.py` 与 `_geo/vol1/utils.py`）
- `PropositionI_3.py` 两份同名同类、内容高度重叠
- `LogoScene` 出现三次：两份 utils.py + `assets/logo/logo.py`
- `README.md` 两份内容完全相同（实为 Python 学习笔记）
- `manim.cfg` 两份内容完全相同

#### P3. 无包结构 / 导入方式脆弱
- 全部使用 `from utils import *`，依赖脚本所在目录为 CWD
- 项目根、`_2024/`、`_geo/`、`_test/` 均无 `__init__.py`
- 跨命题复用 `LogoScene` 必须复制粘贴

### 🟠 中等问题

#### P4. 目录命名混乱、语义不清
- 下划线前缀 `_2024` / `_2025` / `_geo` / `_test` 不规范
- 同一项目三种组织维度并存：按年份、按主题、按用途
- `_test/_test_f` 双重下划线 + 无意义后缀
- 命名风格不一：`v1_Geometry_Fundamentals` vs `vol1` vs `_embedding`

#### P5. Git 跟踪了已不存在的路径
- 跟踪中的 `_test/test_first/`、`_test/test_second/` 在工作树中已不存在

#### P6. 配置文件含硬编码绝对路径，不可移植
- `manim.cfg` 中 `ffmpeg_executable = D:\ProgramFiles\ffmpeg\bin`
- `path = D:\soft\texlive\2024\bin\windows\pdflatex.exe`
- 换机即失效

#### P7. `LogoScene.play_logo_animation` 设计缺陷
- `@staticmethod` 与参数 `self` 自相矛盾
- 调用 `LogoScene.play_logo_animation(self)` 是为绕过此矛盾，属反模式

### 🟡 轻度问题

#### P8. 无效/占位文件
- `main.py` 是 PyCharm 默认模板，无实际用途
- `vector.py` 只有 `pass`
- 多个 `__init__.py` 为 0 字节空文件

#### P9. 无依赖管理
- 缺少 `requirements.txt` / `pyproject.toml`，未锁定 manim/numpy 版本

#### P10. README 内容错位
- 项目根 README 把 Python 基础学习笔记当文档，与项目主题（Manim 动画）无关

#### P11. 无真正的测试
- `_test` 目录实为学习实验场，非单元测试

---

## 三、整改目标

1. **去重**：三份 `LogoScene` → 一份；两份 `utils.py` → 一份；两份 `PropositionI_3.py` → 一份
2. **规整结构**：按"共享代码 / 卷 / 实验"三层组织
3. **工程化**：补齐 `.gitignore` / `requirements.txt` / 真正的 README
4. **可移植**：移除 `manim.cfg` 硬编码绝对路径
5. **瘦身**：清理 1455 个媒体产物、6 个 pyc、`.idea`

---

## 四、分阶段执行方案

### 阶段一：清理（低风险）

#### 1.1 新增 `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*.pyc

# Manim 生成的媒体产物
media/
**/media/
*.mp4
*.svg
*.tex
partial_movie_files/

# IDE
.idea/
.vscode/
*.iml

# 系统
.DS_Store
Thumbs.db
```

#### 1.2 从 git 索引移除（保留本地文件）

```powershell
git rm -r --cached .idea/
git rm -r --cached _2024/v1_Geometry_Fundamentals/media/
git rm -r --cached _2024/v1_Geometry_Fundamentals/__pycache__/
git rm -r --cached assets/logo/media/
git rm --cached _test/test_first/__pycache__/first.cpython-311.pyc
git rm --cached _test/test_first/__pycache__/second.cpython-311.pyc
git rm --cached _test/test_second/__pycache__/test_1.cpython-311.pyc
```

#### 1.3 移除失效路径
- `_test/test_first/` 与 `_test/test_second/` 在工作树中已不存在，但 git 仍跟踪

#### 1.4 删除无意义文件
- `main.py`（PyCharm 模板）
- `_2025/_embedding/vector.py`（仅 `pass`）
- `_test/_test_f/worldquant.py`（无关量化脚本）

---

### 阶段二：去重与重组（核心）

#### 2.1 目标目录结构

```
Euclid/
├── .gitignore
├── README.md                      # 重写真正的项目说明
├── requirements.txt
├── manim.cfg                      # 全局唯一配置
├── REFACTOR_PLAN.md               # 本文档
├── common/                        # 共享代码
│   ├── __init__.py
│   ├── math_utils.py              # MathUtils（唯一）
│   └── scenes.py                  # LogoScene（唯一，修正设计）
├── assets/
│   └── logo/                      # 静态资源目录
├── vol1_geometry/                 # 第一卷 几何基础
│   ├── __init__.py
│   ├── proposition_1.py
│   ├── proposition_2.py
│   ├── proposition_3.py           # 合并两版差异
│   └── proposition_4.py
├── experiments/                   # 学习/试验脚本
│   ├── __init__.py
│   ├── 2024_11_02.py
│   ├── first.py
│   └── second.py
└── docs/
    └── notes.md                   # 原 README 的 Python 学习笔记
```

#### 2.2 创建 `common/math_utils.py`

从两份 `utils.py` 中提取 `MathUtils` 类（`distance`、`find_intersection_points`），合并到唯一文件。

#### 2.3 创建 `common/scenes.py`

修正 `LogoScene.play_logo_animation` 设计：
- 删除 `@staticmethod` 装饰器
- 改为实例方法，签名 `def play_logo_animation(self)` 中 `self` 是 `LogoScene` 实例自身
- 或者改为独立函数 `play_logo_animation(scene: Scene)`，更清晰

合并三份 LogoScene 的差异：以 `_geo/vol1/utils.py` 版本为基准（含 BLUE 高亮色），保留 `assets/logo/logo.py` 中独立的 `wait(2)` 时长调整。

#### 2.4 合并 `PropositionI_3.py` 两版

以 `_geo/vol1/PropositionI_3.py`（21KB，更新版，含 WZ 线段演示）为基准，吸收 `_2024` 版独有的 `find_line_circle_intersection`、`show_proof` 方法（如果 _geo 版缺失）。

#### 2.5 重命名规范
- `PropositionI_1.py` → `proposition_1.py`（小写下划线）
- `v1_Geometry_Fundamentals` → `vol1_geometry`

#### 2.6 统一 `manim.cfg`
- 删除 `_2024/v1_Geometry_Fundamentals/manim.cfg`（重复）
- 修改根 `manim.cfg`：注释掉 `ffmpeg_executable` 与 `latex.path`，提示使用环境变量或 PATH

---

### 阶段三：工程化（中长期）

#### 3.1 添加 `requirements.txt`

```
manim>=0.18.0
numpy>=1.24.0
```

#### 3.2 重写 `README.md`

包含：
- 项目简介（基于 Manim 复刻《几何原本》动画）
- 目录结构说明
- 安装步骤（Python / Manim / LaTeX）
- 运行命令示例
- 配置文件说明

#### 3.3 整理学习笔记到 `docs/notes.md`

原 README 中的 day09/10/11 Python 笔记挪到这里，与项目主文档分离。

---

## 五、执行进度跟踪

| 步骤 | 状态 | 备注 |
| --- | --- | --- |
| 创建本方案文档 | ✅ 完成 | REFACTOR_PLAN.md |
| 阶段一 1.1 创建 .gitignore | ✅ 完成 | 覆盖 pyc/media/.idea/.vscode 等 |
| 阶段一 1.2 git rm --cached 媒体/pyc/.idea | ✅ 完成 | 724+ 项从索引移除，本地保留 |
| 阶段一 1.3 移除失效路径 | ✅ 完成 | _test/test_first、_test/test_second 随目录删除 |
| 阶段一 1.4 删除无意义文件 | ✅ 完成 | main.py / vector.py / worldquant.py / 空 _2025 |
| 阶段二 2.1 创建目标目录 | ✅ 完成 | common/ vol1_geometry/ experiments/ docs/ |
| 阶段二 2.2 合并 utils.py → common/math_utils.py | ✅ 完成 | MathUtils 唯一来源 |
| 阶段二 2.3 合并 LogoScene → common/scenes.py | ✅ 完成 | 改为 play_logo_animation(scene) 函数 |
| 阶段二 2.4 合并 PropositionI_3 两版 | ✅ 完成 | 以 _geo 版为基准，保留 WZ 演示与扩展证明 |
| 阶段二 2.5 命名规范化 | ✅ 完成 | PropositionI_*.py → proposition_*.py |
| 阶段二 2.6 统一 manim.cfg | ✅ 完成 | 根 manim.cfg，注释 ffmpeg/latex 硬编码路径 |
| 阶段二 2.7 迁移 experiments | ✅ 完成 | first.py / second.py / 2024_11_02.py |
| 阶段二 2.8 删除旧目录 | ✅ 完成 | _geo / _2024 / _test 已删除 |
| 阶段三 3.1 requirements.txt | ✅ 完成 | manim>=0.18.0, numpy>=1.24.0 |
| 阶段三 3.2 重写 README | ✅ 完成 | 项目说明 / 目录 / 安装 / 运行 / 配置 |
| 阶段三 3.3 docs/notes.md | ✅ 完成 | 原 Python 笔记与 manim 命令说明合并 |

---

## 六、风险与建议

| 阶段 | 风险 | 建议 |
| --- | --- | --- |
| 阶段一 | 低，纯清理 | 立即执行 |
| 阶段二 | 中，涉及代码合并与路径变更 | 逐文件 diff 比对，分命题单独迁移并验证渲染 |
| 阶段三 | 低 | 渐进推进 |

**关键提醒**：阶段二合并 `PropositionI_3.py` 时，需以 `_geo/vol1/PropositionI_3.py`（21KB，更新版）为基准，吸收 `_2024` 版中独有的逻辑（如 `show_proof` 证明文本动画），避免功能丢失。
