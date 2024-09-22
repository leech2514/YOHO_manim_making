import numpy as np
from manim import *
"""
This file contains the MathUtils class which contains static methods for mathematical operations.
"""
class MathUtils:
    @staticmethod
    def distance(x1, y1, x2, y2):
        """
        Calculate the distance between two points (x1, y1) and (x2, y2).
        :param x1: x-coordinate of the first point
        :param y1: y-coordinate of the first point
        :param x2: x-coordinate of the second point
        :param y2: y-coordinate of the second point
        :return: Returns the distance between the two points.
        """
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    @staticmethod
    def find_intersection_points(A, B, r):
        """
        Find the intersection points of two circles with centers A and B and radius r.
        :param A:  A is the centers of the circles
        :param B:  B is the centers of the circle
        :param r:  r is the radius of the circles
        :return: Returns the intersection points of the two circles.
        """
        """
        什么是静态方法？如何使用？
        @staticmethods 是一个装饰器，用来定义静态方法。不需要self参数，可以直接通过类名调用。只依赖传入的参数，不依赖于实例的状态。
        1.可直接被调用，不需要实例化对象：如math.sqrt(x)
        """
        d = np.linalg.norm(B - A)
        a = (r ** 2 - r ** 2 + d ** 2) / (2 * d)
        h = np.sqrt(r ** 2 - a ** 2)
        P2 = A + a * (B - A) / d
        intersection1 = P2 + h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        intersection2 = P2 - h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        return [intersection1, intersection2]


"""
视频开头的 logo 动画效果
"""
class LogoScene(Scene):
    @staticmethod
    def play_logo_animation(self):
        """
        创建‘《几何原本》’和‘YOHO’的 logo 动画效果，主要用在每个视频的开头。
        版本暂定为 v1.0
        调用方法：LogoScene.play_logo_animation(self)
        :param self:
        :return:
        """
        # 创建渐变背景
        background: Rectangle = Rectangle(width=config.frame_width, height=config.frame_height).set_fill(WHITE, opacity=1)
        self.add(background)

        geometry_text: Text = Text("《几何原本》", font_size=80, weight=BOLD)
        geometry_background = RoundedRectangle(corner_radius=0.2, height=geometry_text.height + 0.5,
                                               width=geometry_text.width + 0.5, stroke_color=BLACK, stroke_width=4)
        geometry_background.set_fill(BLACK, opacity=0.7)
        geometry_text.move_to(geometry_background.get_center())

        self.play(DrawBorderThenFill(geometry_background))
        self.play(Write(geometry_text))
        self.wait(2)

        # 创建文本 logo
        logo_text: Text = Text("YOHO", font_size=15, weight=BOLD)
        logo_text.set_color(WHITE)

        # 添加边框和阴影
        logo_background: RoundedRectangle = RoundedRectangle(corner_radius=0.4, height=logo_text.height + 0.5, width=logo_text.width + 0.5, stroke_color=BLACK, stroke_width=4)
        logo_background.set_fill(BLACK, opacity=0.7)

        logo_background.move_to(1.2 * UP + 2.1 * LEFT)
        logo_text.move_to(logo_background.get_center())

        self.play(DrawBorderThenFill(logo_background))
        self.play(Write(logo_text))
        self.wait(2)

        self.play(logo_text.animate.scale(1.2).set_color(RED), run_time=0.5)
        self.play(logo_text.animate.scale(1 / 1.1).set_color(BLACK), run_time=0.5)

        # 结束场景
        self.play(
            FadeOut(background),
            FadeOut(logo_background),
            FadeOut(geometry_background),
            FadeOut(logo_text),
            FadeOut(geometry_text),
            runtime=1
        )

