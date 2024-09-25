import os

from manim import *
from utils import *

"""
Proposition I.3: 设直线AB与直线AC平行，且直线AB与直线AC的交点为E，则有AE = c
"""
class VolumeIPropositionIII(Scene):
    def construct(self):
        # 添加logo动画
        logo_scene = LogoScene()
        logo_scene.play_logo_animation(self)

        # 创建较长的线段AB
        A = np.array([0, 0, 0])
        B = np.array([3, 0, 0])
        AB = Line(A, B, color=BLUE)
        A_dot = Dot(A)
        B_dot = Dot(B)
        A_label = Text("A", font_size=25).next_to(A, LEFT)
        # 创建一个文本对象“B”，并将其字体大小设置为25，然后将其放置在对象B的下方

        B_label = Text("B", font_size=25).next_to(B, DOWN)

        text_1 = Text("设直线AB与直线AC平行，且直线AB与直线AC的交点为E，则有AE = c", font_size=25)\
            .to_edge(UP + LEFT, buff=0.5)

        self.play(Write(text_1))

        # 3D,旋转text_1的文本360度,展示动画效果

        # self.set_camera_orientation(phi=0 * DEGREES, theta=-60 * DEGREES, gamma=60 * DEGREES, distance=200)
        # self.play(text_1.animate.rotate(360 * DEGREES, axis=UP))

        # 创建较短的线段AC，方向不同于AB
        c_length = 2
        C = A + np.array([0, -c_length, 0])
        AC = Line(A, C, color=GREEN)
        C_dot = Dot(C)
        C_label = Text("C", font_size=25).next_to(C, DOWN)

        # 构造圆DEF，圆心与A重合
        circle = Circle(radius=c_length, color=YELLOW).move_to(A)

        # 圆与线段AB的交点E
        E = A + np.array([c_length, 0, 0])  # E在AB上
        E_dot = Dot(E, color=RED)
        E_label = Text("E", font_size=25).next_to(E, DOWN + LEFT)

        # 添加到场景
        self.play(Create(AB), Create(A_dot), Create(B_dot), Write(A_label), Write(B_label))
        self.play(Create(AC), Create(C_dot), Write(C_label))
        self.play(Create(circle))
        self.play(Create(E_dot), Write(E_label))

        # 高亮线段AE
        AE = Line(A, E, color=RED)
        self.play(Create(AE))

        # 标注AE和c相等
        AE_label = Text("AE = c", font_size=25).next_to(AE, UP)
        self.play(Write(AE_label))

        self.wait()
        soul = VGroup(text_1, AB, A_dot, B_dot, A_label, B_label, AC, C_dot, C_label, circle, E_dot, E_label, AE, AE_label)
        self.play(FadeOut(soul))

        """
            video11.construct()  并不能正确调用播放第二个动画：Manim是通过事件驱动的机制（如self.play()）来处理动画的；
            因此在另一个场景中调用另一个场景的构造函数，并不会触发动画的播放。
        """
        # 第二种情况
        # video11 = VolumeIPropositionII()
        # video11.construct()  # 调用第二个场景的构造函数，并不会触发动画的播放。
        # self.add(video11)  # 直接将第二个场景添加到当前场景中，并不会触发动画的播放。
        # video11.play_animation(self)  # AttributeError: 'VolumeIPropositionII' object has no attribute 'play_animation'

        A = np.array([0, 0, 0])
        B = np.array([0.7, 0.5, 0])
        C = np.array([0.7, 2.5, 0])
        P = np.array([0, -2, 0])

        dot_A = Dot(point=A, color=RED)
        dot_B = Dot(point=B, color=YELLOW)
        dot_C = Dot(point=C, color=YELLOW)
        dot_P = Dot(point=P, color=RED)

        label_A = Text('A', font_size=24).next_to(A, LEFT)
        label_B = Text('B', font_size=24).next_to(B, RIGHT+UP, buff=0.2)
        label_C = Text('C', font_size=24).next_to(C, UP)
        label_P = Text('P', font_size=24).next_to(P, DOWN)

        line_BC = Line(start=B, end=C)
        line_AP = Line(start=A, end=P)

        #text_1 = Text('《几何原本》 第一卷 命题II', font_size=35)
        text_2 = Text('命题II：从一个给定的点可以引一条线段等于已知线段', font_size=35)
        # line_spacing 调整行间距
        text_3 = Text(
            '命题II：\n'
            '从一个给定的点可以引 \n'
            '一条线段等于已知线段',
            font_size=20, line_spacing=1).to_edge(LEFT + UP, buff=1)

        # self.play(FadeIn(text_1, run_time=3))
        # self.wait(2)
        #self.play(FadeOut(text_1))

        self.play(FadeIn(text_2, run_time=5))
        self.wait(0.5)
        self.play(FadeOut(text_2))

        self.play(FadeIn(text_3, run_time=5))
        self.wait(0.5)
        # self.play(FadeOut(text_2))

        self.play(FadeIn(dot_A), Write(label_A))
        self.wait(1)
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))
        # self.wait(1)
        self.play(Create(line_BC, run_time=2))
        self.wait(1)

        self.play(FadeIn(dot_P), Write(label_P))
        self.wait(1)
        self.play(Create(line_AP, run_time=2))
        self.wait(5)

        self.play(FadeOut(dot_P), FadeOut(line_AP), FadeOut(label_P))
        self.wait(6)

        # 基于命题一，作等边三角形
        # 连接A/B
        line_AB = Line(start=A, end=B)
        self.play(Create(line_AB, run_time=1))
        circle1 = Circle(radius=line_AB.get_length(), color=GREEN, arc_center=A)
        circle2 = Circle(radius=line_AB.get_length(), color=YELLOW, arc_center=B)

        anim_group1 = AnimationGroup(
            Create(circle1, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=A, run_time=4)
        )
        self.play(anim_group1)
        # self.play(FadeIn(dot_F, running_start=2), Write(label_F))
        self.wait(2)

        anim_group2 = AnimationGroup(
            Create(circle2, run_time=4),
            Rotate(line_AB, angle=2*PI, about_point=B, run_time=4)
        )
        self.play(anim_group2)
        # self.play(FadeIn(dot_E, running_start=2), Write(label_E))
        self.wait(2)

        intersection_points = self.find_intersection_points(A, B, line_AB.get_length())
        if len(intersection_points) == 2:
            dot_D = Dot(point=intersection_points[0], color=BLUE)
            label_D = Text('D', font_size=24).next_to(dot_D, LEFT + UP)

            self.play(FadeIn(dot_D), Write(label_D))
            self.wait(2)

        line_AD = Line(start=B, end=intersection_points[0])
        line_BD = Line(start=A, end=intersection_points[0])
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
        direction_DA = A - intersection_points[0]
        direction_DB = B - intersection_points[0]
        extend_ratio = 3  # 延长的比例，可以调整
        extended_dot_E = A + extend_ratio * direction_DA
        extended_dot_F = B + extend_ratio * direction_DB
        dot_E = Dot(point=extended_dot_E, color=RED)
        dot_F = Dot(point=extended_dot_F, color=RED)
        # extended_line_DA = Line(start=A_shifted, end=dot_E + shift_vector, color=GREEN)
        # extended_line_DB = Line(start=B_shifted, end=dot_F + shift_vector, color=GREEN)
        extended_line_DA = Line(start=A, end=dot_E, color=RED)
        extended_line_DB = Line(start=B, end=dot_F, color=RED)

        label_E = Text('E', font_size=24).next_to(dot_E, DOWN)
        label_F = Text('F', font_size=24).next_to(dot_F, RIGHT)

        self.play(Create(extended_line_DA, run_time=2))
        self.play(FadeIn(dot_E), Write(label_E))
        self.wait(1)
        self.play(Create(extended_line_DB, run_time=2))
        self.play(FadeIn(dot_F), Write(label_F))
        self.wait(3)

        circle3 = Circle(radius=line_BC.get_length(), color=GREEN, arc_center=B)

        anim_group4 = AnimationGroup(
            Create(circle3, run_time=4),
            Rotate(line_BC, angle=2*PI, about_point=B, run_time=4)
        )
        self.play(anim_group4)
        self.wait(3)

        # 找到circle3和线段BF的交点
        intersection_with_BF = self.find_line_circle_intersection(B, extended_dot_F, B, line_BC.get_length())

        if len(intersection_with_BF) > 0:
            dot_G = Dot(point=intersection_with_BF[0], color=PURPLE)
            label_G = Text('G', font_size=24).next_to(dot_G, DOWN)
            line_DG = Line(start=intersection_points[0], end=dot_G)
            self.play(FadeIn(dot_G), Write(label_G))
            self.wait(3)

            # 以D为圆心，DG为半径作圆
            circle4 = Circle(radius=np.linalg.norm(intersection_points[0] - intersection_with_BF[0]), color=ORANGE, arc_center=intersection_points[0])
            anim_group5 = AnimationGroup(
                Create(circle4, run_time=4),
                Rotate(line_DG, angle=2*PI, about_point=intersection_points[0], run_time=4)
            )
            self.play(anim_group5)
            self.play(FadeOut(line_DG))
            self.wait(1)

            # 找到circle4和线段DE的交点
            intersection_with_DE = self.find_line_circle_intersection(intersection_points[0], extended_dot_E, intersection_points[0], np.linalg.norm(intersection_points[0] - intersection_with_BF[0]))

            if len(intersection_with_DE) > 0:
                dot_L = Dot(point=intersection_with_DE[0], color=TEAL)
                label_L = Text('L', font_size=24).next_to(dot_L, LEFT + UP, buff=0.2)
                self.play(FadeIn(dot_L), Write(label_L))
                self.wait(3)

            # 计算移动向量
            move_vector = 3 * RIGHT
            move_vector1 = 3 * LEFT
            # 移动所有对象
            self.play(
                AnimationGroup(
                    ApplyMethod(dot_A.shift, move_vector),
                    ApplyMethod(dot_B.shift, move_vector),
                    ApplyMethod(dot_C.shift, move_vector),
                    ApplyMethod(dot_D.shift, move_vector),
                    ApplyMethod(dot_E.shift, move_vector),
                    ApplyMethod(dot_F.shift, move_vector),
                    ApplyMethod(dot_G.shift, move_vector),
                    ApplyMethod(dot_L.shift, move_vector),
                    ApplyMethod(label_A.shift, move_vector),
                    ApplyMethod(label_B.shift, move_vector),
                    ApplyMethod(label_C.shift, move_vector),
                    ApplyMethod(label_D.shift, move_vector),
                    ApplyMethod(label_E.shift, move_vector),
                    ApplyMethod(label_F.shift, move_vector),
                    ApplyMethod(label_G.shift, move_vector),
                    ApplyMethod(label_L.shift, move_vector),
                    ApplyMethod(circle3.shift, move_vector),
                    ApplyMethod(circle4.shift, move_vector),
                    ApplyMethod(line_AB.shift, move_vector),
                    ApplyMethod(line_AD.shift, move_vector),
                    ApplyMethod(line_BC.shift, move_vector),
                    ApplyMethod(line_BD.shift, move_vector),
                    ApplyMethod(extended_line_DB.shift, move_vector),
                    ApplyMethod(extended_line_DA.shift, move_vector),
                    lag_ratio=0,  # 无延迟
                ),
                run_time=2
            )

            A_shifted = A + np.array([3, 0, 0])
            C_shifted = C + np.array([3, 0, 0])
            B_shifted = B + np.array([3, 0, 0])
            G_shifted = intersection_with_BF[0] + np.array([3, 0, 0])
            L_shifted = intersection_with_DE[0] + np.array([3, 0, 0])

            shifted_line_AL = Line(start=A_shifted, end=L_shifted)
            shifted_line_BG = Line(start=B_shifted, end=G_shifted)
            shifted_line_BC = Line(start=B_shifted, end=C_shifted)
            # 改变线段颜色
            self.play(
                shifted_line_BC.animate.set_color(BLUE),
                shifted_line_AL.animate.set_color(BLUE),
                shifted_line_BG.animate.set_color(BLUE),
                run_time=2
            )
            self.wait(11)

            # 展示证明过程
            all_texts = self.show_proof()
            self.wait(5)

        self.play(*[FadeOut(text) for text in all_texts])
        self.wait(5)

        # 移动所有对象
        self.play(
            AnimationGroup(
                ApplyMethod(dot_A.shift, move_vector1),
                ApplyMethod(dot_B.shift, move_vector1),
                ApplyMethod(dot_C.shift, move_vector1),
                ApplyMethod(dot_D.shift, move_vector1),
                ApplyMethod(dot_E.shift, move_vector1),
                ApplyMethod(dot_F.shift, move_vector1),
                ApplyMethod(dot_G.shift, move_vector1),
                ApplyMethod(dot_L.shift, move_vector1),
                ApplyMethod(label_A.shift, move_vector1),
                ApplyMethod(label_B.shift, move_vector1),
                ApplyMethod(label_C.shift, move_vector1),
                ApplyMethod(label_D.shift, move_vector1),
                ApplyMethod(label_E.shift, move_vector1),
                ApplyMethod(label_F.shift, move_vector1),
                ApplyMethod(label_G.shift, move_vector1),
                ApplyMethod(label_L.shift, move_vector1),
                ApplyMethod(circle3.shift, move_vector1),
                ApplyMethod(circle4.shift, move_vector1),
                ApplyMethod(line_AB.shift, move_vector1),
                ApplyMethod(line_AD.shift, move_vector1),
                ApplyMethod(line_BC.shift, move_vector1),
                ApplyMethod(line_BD.shift, move_vector1),
                ApplyMethod(extended_line_DB.shift, move_vector1),
                ApplyMethod(extended_line_DA.shift, move_vector1),
                ApplyMethod(shifted_line_AL.shift, move_vector1),
                ApplyMethod(shifted_line_BG.shift, move_vector1),
                ApplyMethod(shifted_line_BC.shift, move_vector1),
                lag_ratio=0,  # 无延迟
            ),
            run_time=2
        )
        self.wait(5)


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

    def find_line_circle_intersection(self, A, B, C, r):
        # A and B are the endpoints of the line segment
        # C is the center of the circle
        # r is the radius of the circle
        BA = B - A
        CA = C - A
        a = np.dot(BA, BA)
        b = 2 * np.dot(BA, CA)
        c = np.dot(CA, CA) - r * r
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []

        t1 = (-b + np.sqrt(discriminant)) / (2 * a)
        t2 = (-b - np.sqrt(discriminant)) / (2 * a)

        points = []
        if 0 <= t1 <= 1:
            points.append(A + t1 * BA)
        if 0 <= t2 <= 1:
            points.append(A + t2 * BA)

        return points

    def show_proof(self):
        # 证明过程中的文本内容和动画
        sentences = [
            "∵ B点是圆BCG的圆心，故BC = BG",
            "又，因为D点是圆DGL的圆心，故DL = DG",
            "∵ DA = DB，其余下部分AL = BG",
            "同理可证：BC = BG",
            "∴ 线段AL = BC = BG",
            "等量减等量，差相等",
            "∴ AL = BC",
            "∴ 从给定的点A作出的线段AL等于给定的线段BC",
            "证完;"
        ]

        # 创建文本对象并播放动画
        prev_text = None
        all_texts = []
        for sentence in sentences:
            text = Text(sentence, font_size=20)
            if prev_text is None:
                text.to_edge(5 * DOWN + LEFT, buff=1)
            else:
                text.next_to(prev_text, DOWN)
                text.align_to(prev_text, LEFT)
            self.play(Write(text))
            self.wait(3.5)

            all_texts.append(text)
            prev_text = text
        return all_texts


if __name__ == '__main__':
    scene = VolumeIPropositionIII()
    scene.render()
