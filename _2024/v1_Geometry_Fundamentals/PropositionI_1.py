from manim import *
import numpy as np
"""
    已知一条线段可作一个等边三角形。
    设：AB为已知的线段。
    要求：以线段AB为边建立一个等边三角形，以A为圆心、AB为半径作圆BCD；再以B为圆心、以BA为半径作圆ACE；两圆相交于C点，连接CA、CB。
"""


class VolumeIPropositionI(Scene):
    def construct(self):
        A = np.array([-1, 0, 0])
        B = np.array([1, 0, 0])

        F = A + (A - B)
        E = B + (B - A)

        dot_A = Dot(point=A, color=GREEN)
        dot_B = Dot(point=B, color=YELLOW)
        dot_F = Dot(point=F, color=GREEN)
        dot_E = Dot(point=E, color=YELLOW)

        line_AB = Line(start=A, end=B)

        label_A = Text('A', font_size=24).next_to(A, LEFT)
        label_B = Text('B', font_size=24).next_to(B, RIGHT)
        label_F = Text('F', font_size=24).next_to(F, LEFT)
        label_E = Text('E', font_size=24).next_to(E, RIGHT)

        circle1 = Circle(radius=line_AB.get_length(), color=GREEN, arc_center=A)
        circle2 = Circle(radius=line_AB.get_length(), color=YELLOW, arc_center=B)

        self.play(FadeIn(dot_A, running_start=1), Write(label_A))
        self.wait(1)
        self.play(FadeIn(dot_B, running_start=1), Write(label_B))

        self.play(Create(line_AB, run_time=4))

        anim_group1 = AnimationGroup(
            Create(circle1, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=A, run_time=4)
        )
        self.play(anim_group1)
        self.play(FadeIn(dot_F, running_start=2), Write(label_F))
        self.wait(2)

        anim_group2 = AnimationGroup(
            Create(circle2, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=B, run_time=4)
        )
        self.play(anim_group2)
        self.play(FadeIn(dot_E, running_start=2), Write(label_E))
        self.wait(2)

        intersection_points = self.find_intersection_points(A, B, line_AB.get_length())
        if len(intersection_points) == 2:
            dot_C = Dot(point=intersection_points[0], color=BLUE)
            label_C = Text('C', font_size=24).next_to(dot_C, UP)
            dot_D = Dot(point=intersection_points[1], color=GREEN)
            label_D = Text('D', font_size=24).next_to(dot_D, DOWN)

            self.play(FadeIn(dot_C), Write(label_C))
            self.play(FadeIn(dot_D), Write(label_D))
            self.wait(2)

            line_CA = Line(start=A, end=intersection_points[0])
            line_CB = Line(start=B, end=intersection_points[0])

            self.play(Create(line_CA, run_time=2))
            self.play(Create(line_CB, run_time=2))
            self.wait(3)

        anim_group3 = AnimationGroup(
            line_AB.animate.set_color(RED),
            line_CB.animate.set_color(RED),
            line_CA.animate.set_color(RED),
            lag_ratio=0
        )

        self.play(anim_group3, run_time=3)
        self.wait(3)

        self.play(
            ApplyMethod(circle1.set_stroke, None, 0.4),  # 进一步减少圆1的填充透明度
            ApplyMethod(circle2.set_stroke, None, 0.4),  # 进一步减少圆2的填充透明度
            run_time=2
        )
        self.wait(3)

        self.move_scene_elements()
        self.wait(2)

        # 展示证明过程
        self.show_proof()

        self.wait(10)

    def show_proof(self):
        # 证明过程中的文本内容和动画
        sentences = [
            "∵ A点是圆CDB的圆心，故AC = AB",
            "又，点B是圆CAE的圆心，故BC = BA，CA = AB",
            "∴ CA = CB = AB",
            "∵ 等于同量的量互相相等",
            "∴ CA = CB",
            "∴ 三条线段CA、AB、BC相等",
            "∴ 三角形ABC是建立在线段AB上的等边三角形",
            "证完;"
        ]

        # 创建文本对象并播放动画
        prev_text = None
        for sentence in sentences:
            text = Text(sentence, font_size=24)
            if prev_text is None:
                text.to_edge(4*DOWN + 2 * RIGHT, buff=1)
            else:
                text.next_to(prev_text, DOWN)
                text.align_to(prev_text, LEFT)
            self.play(Write(text))
            self.wait(2)
            prev_text = text

    def move_scene_elements(self):
        # 移动整个场景中的元素向左上方
        move_vector = 2.7 * LEFT + 1.7 * UP
        for mob in self.mobjects:
            self.play(
                ApplyMethod(mob.shift, move_vector),
                run_time=0.00001
            )

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
    scene = VolumeIPropositionI()
    scene.render()

