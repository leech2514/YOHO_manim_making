# Render

基于 [Manim](https://www.manim.community/) 动画引擎复刻《几何原本》（Euclid's Elements）的几何命题演示项目。

---

## 项目简介

本项目使用 Manim 将《几何原本》第一卷的几何命题逐条制作为可视化动画，
每条命题包含：命题陈述 → 几何作图 → 推理证明 → 结论。

第一卷已完成命题：

| 命题       | 主题                               | 场景类                    |
| ---------- | ---------------------------------- | ------------------------- |
| I.1        | 在已知线段上作等边三角形           | `VolumeIPropositionI`     |
| I.2        | 从给定点引一线段等于已知线段       | `VolumeIPropositionII`    |
| I.3        | 在较长线段上截取等于较短线段       | `VolumeIPropositionIII`   |
| I.4        | 边角边（SAS）全等定理              | `VolumeIPropositionIV`    |

---

## 目录结构

```
Render/
├── .gitignore
├── README.md                      # 本文件
├── requirements.txt               # Python 依赖
├── manim.cfg                      # 全局 Manim 配置
├── CONTRIBUTING.md                # 项目开发规范（命名 / import / Scene 范式）
├── REFACTOR_PLAN.md               # 项目结构整改方案（历史记录）
├── common/                        # 共享代码
│   ├── __init__.py
│   ├── math_utils.py              # MathUtils（distance / 圆交点 / 线圆交点）
│   └── scenes.py                  # play_logo_animation（开头 logo 动画）
├── vol1_geometry/                 # 第一卷 几何基础
│   ├── __init__.py
│   ├── proposition_1.py
│   ├── proposition_2.py
│   ├── proposition_3.py           # 合并 _geo / _2024 两版
│   └── proposition_4.py
├── experiments/                   # 学习与试验脚本
│   ├── __init__.py
│   ├── 2024_11_02.py
│   ├── first.py
│   └── second.py
├── assets/
│   └── logo/                      # 静态资源占位目录
└── docs/
    └── notes.md                   # Python / Manim / LaTeX 学习笔记
```

---

## 安装步骤

### 1. 安装 Python

Python 3.9+，建议使用 3.11。

### 2. 安装 Manim 及依赖

```bash
pip install -r requirements.txt
```

Manim 完整安装说明见官方文档：https://docs.manim.community/en/stable/installation.html

### 3. 安装 LaTeX（用于渲染数学公式）

- Windows 推荐 TeX Live 或 MiKTeX
- 安装后确保 `pdflatex` 在系统 PATH 中可用
- 若使用默认 PATH，无需修改 `manim.cfg`；若需指定绝对路径，编辑 `manim.cfg` 的 `[latex]` 段
- 排错见 [docs/notes.md](docs/notes.md) 第二节

### 4. 安装 ffmpeg（用于渲染视频）

- Manim 需要 ffmpeg。Windows 可从 https://ffmpeg.org/download.html 下载
- 确保 `ffmpeg` 在系统 PATH 中可用
- 若需指定绝对路径，编辑 `manim.cfg` 的 `[ffmpeg]` 段

---

## 运行命令

在项目根目录执行：

```bash
# 低质量预览（开发调试）
manim -p -ql vol1_geometry/proposition_1.py VolumeIPropositionI

# 高质量渲染（最终输出）
manim -p -qh vol1_geometry/proposition_3.py VolumeIPropositionIII
```

参数说明：

- `-p` ：渲染完毕自动预览
- `-ql / -qm / -qh` ：低 / 中 / 高 质量
- `-r 1920,1080` ：手动指定分辨率
- `--fps 60` ：手动指定帧率

更多命令示例见 [docs/notes.md](docs/notes.md) 第一节。

---

## 配置文件说明

`manim.cfg` 为项目全局配置，主要项：

| 配置项              | 默认值                  | 说明                                  |
| ------------------- | ----------------------- | ------------------------------------- |
| `renderer`          | `cairo`                 | 渲染器（cairo / opengl）              |
| `frame_rate`        | `60`                    | 帧率                                  |
| `pixel_height/width`| `1080 / 1920`           | 输出分辨率                            |
| `background_color`  | `BLACK`                 | 背景色                                |
| `media_dir`         | `./media`               | 媒体产物输出目录（已加入 .gitignore） |
| `ffmpeg_executable` | （注释，依赖 PATH）     | ffmpeg 可执行文件路径                  |
| `latex.path`        | （注释，依赖 PATH）     | pdflatex 可执行文件路径                |

> **可移植性**：原项目中硬编码的 `D:\ProgramFiles\...` 与 `D:\soft\texlive\...`
> 绝对路径已注释，改为依赖系统 PATH。换机无需修改配置即可运行。

---

## 共享代码说明

### `common.math_utils.MathUtils`

几何计算工具，全部为静态方法：

- `distance(x1, y1, x2, y2)`：两点欧氏距离
- `find_intersection_points(A, B, r)`：两等圆（圆心 A、B，半径 r）的交点
- `find_line_circle_intersection(A, B, C, r)`：线段 AB 与圆（圆心 C，半径 r）的交点

### `common.scenes.play_logo_animation(scene)`

视频开头《几何原本》+ YOHO logo 动画。在 Scene 中调用：

```python
from common.scenes import play_logo_animation

class MyScene(Scene):
    def construct(self):
        play_logo_animation(self)
        # ... 后续动画
```

---

## 项目历史

本项目经历过一次结构整改，整改前的状态与方案记录于 [REFACTOR_PLAN.md](REFACTOR_PLAN.md)。
主要改动：删除 1455 个混入版本库的媒体产物、统一三份重复的 `LogoScene`、
合并两份 `PropositionI_3.py`、规范化目录命名（`_geo` / `_2024` → `vol1_geometry`）、
移除 `manim.cfg` 硬编码绝对路径。

---

## 开发规范

代码贡献请遵循 [CONTRIBUTING.md](CONTRIBUTING.md)，涵盖：

- 目录职责与命名约定（文件名 / 类名 / 函数名）
- Import 规则（Manim 星号导入、common 显式导入、禁止相对导入）
- Scene 编写范式（Logo 调用方式、MathUtils 使用方式、show_proof 归属）
- manim.cfg 可移植性约束
- Git 提交规范与 Checklist
