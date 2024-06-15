from manim import *

"""
    执行的命令：manim -p -ql first.py SquareToCircle
    执行时如果出现权限相关的问题，把电脑的安全软件关一下
"""


class SecondExample(Scene):
    def construct(self):
        # 创建坐标系
        ax = Axes(
            x_range=(-3, 3),
            y_range=(-3, 3),
            axis_config={"color": BLUE}  # 设置轴线的颜色为蓝色
        )

        # 在坐标系创建曲线函数
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2), color=RED)

        # 指定x轴的范围
        area = ax.get_area(curve, x_range=(-2, 0))
        # 以动画的形式展示创建过程
        self.play(Create(ax))
        self.play(Create(curve, run_time=6))
        self.play(FadeIn(area, run_time=3))
        self.wait(2)


class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        # 画出图像的边界，并填充颜色
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        # 代替转换
        self.play(ReplacementTransform(green_square, blue_circle, run_time=6))
        # Indicate是让传入的参数对象变大，颜色为黄色。在吸引观众方面挺有用的
        self.play(Indicate(blue_circle, run_time=4))
        # 对象淡出
        self.play(FadeOut(blue_circle, run_time=4))
        self.wait(2)


if __name__ == "__main__":
    scene = SecondExample()
    scene.render()
