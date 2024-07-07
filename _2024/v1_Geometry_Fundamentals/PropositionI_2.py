from manim import *
import numpy as np
"""
    已知一条线段可作一个等边三角形。
    设：AB为已知的线段。
    要求：以线段AB为边建立一个等边三角形，以A为圆心、AB为半径作圆BCD；再以B为圆心、以BA为半径作圆ACE；两圆相交于C点，连接CA、CB。
"""


class VolumeIPropositionII(Scene):
    def construct(self):
        A = np.array([0, 0, 0])
        B = np.array([0.7, 0.5, 0])
        C = np.array([0.7, 2.5, 0])

        dot_A = Dot(point=A, color=RED)
        dot_B = Dot(point=B, color=YELLOW)
        dot_C = Dot(point=C, color=YELLOW)

        label_A = Text('A', font_size=24).next_to(A, LEFT)
        label_B = Text('B', font_size=24).next_to(B, RIGHT)
        label_C = Text('C', font_size=24).next_to(C, LEFT)

        line_BC = Line(start=B, end=C)

        self.play(FadeIn(dot_A), Write(label_A))
        self.wait(1)
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))
        # self.wait(1)
        self.play(Create(line_BC, run_time=2))
        self.wait(1)

        # 将点A和线段BC向左平移5个单位，再向上平移2个单位
        shift_vector = LEFT * 4
        self.play(
            dot_A.animate.shift(shift_vector),
            label_A.animate.shift(shift_vector),
            line_BC.animate.shift(shift_vector),
            dot_B.animate.shift(shift_vector),
            dot_C.animate.shift(shift_vector),
            label_B.animate.shift(shift_vector),
            label_C.animate.shift(shift_vector)
        )

        self.wait(3)

        # 基于命题一，作等边三角形

        A_shifted = A + np.array([-4, 0, 0])
        B_shifted = B + np.array([-4, 0, 0])
        # 连接A/B
        line_AB = Line(start=A_shifted, end=B_shifted)
        self.play(Create(line_AB, run_time=1))
        circle1 = Circle(radius=line_AB.get_length(), color=GREEN, arc_center=A_shifted)
        circle2 = Circle(radius=line_AB.get_length(), color=YELLOW, arc_center=B_shifted)

        anim_group1 = AnimationGroup(
            Create(circle1, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=A_shifted, run_time=4)
        )
        self.play(anim_group1)
        # self.play(FadeIn(dot_F, running_start=2), Write(label_F))
        self.wait(2)

        anim_group2 = AnimationGroup(
            Create(circle2, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=B_shifted, run_time=4)
        )
        self.play(anim_group2)
        # self.play(FadeIn(dot_E, running_start=2), Write(label_E))
        self.wait(2)

        intersection_points = self.find_intersection_points(A_shifted, B_shifted, line_AB.get_length())
        if len(intersection_points) == 2:
            dot_D = Dot(point=intersection_points[0], color=BLUE)
            label_D = Text('D', font_size=24).next_to(dot_D, LEFT)

            self.play(FadeIn(dot_D), Write(label_D))
            self.wait(2)

        line_AD = Line(start=B_shifted, end=intersection_points[0])
        line_BD = Line(start=A_shifted, end=intersection_points[0])
        self.play(Create(line_AD), Create(line_BD))
        self.play(FadeOut(circle1), FadeOut(circle2))

        # 突出显示三角形ABC
        anim_group3 = AnimationGroup(
            line_AB.animate.set_color(RED),
            line_BD.animate.set_color(RED),
            line_AD.animate.set_color(RED),
            lag_ratio=0
        )
        self.play(anim_group3, run_time=3)
        self.wait(3)

        # 计算 DA 的方向向量并延长线段
        direction_DA = A_shifted - intersection_points[0]
        extend_ratio = 2  # 延长的比例，可以调整
        dot_E = A + extend_ratio * direction_DA
        extended_line_DA = Line(start=A_shifted, end=dot_E + shift_vector, color=GREEN)

        self.play(Create(extended_line_DA, run_time=2))

        self.wait(3)

        self.wait(3)

    def find_intersection_points(self, A, B, r):
        # A and B are the centers of the circles
        # r is the radius of the circles
        d = np.linalg.norm(B - A)
        a = (r ** 2 - r ** 2 + d ** 2) / (2 * d)
        h = np.sqrt(r ** 2 - a ** 2)
        P2 = A + a * (B - A) / d
        intersection1 = P2 + h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        intersection2 = P2 - h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        return [intersection1, intersection2]


if __name__ == '__main__':
    scene = VolumeIPropositionII()
    scene.render()