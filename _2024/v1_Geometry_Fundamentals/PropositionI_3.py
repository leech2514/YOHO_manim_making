import os

from manim import *
from utils import *
"""
Proposition I.3: 设直线AB与直线AC平行，且直线AB与直线AC的交点为E，则有AE = c
"""
class VolumeIPropositionIII(Scene):
    def construct(self):
        # self.renderer.init_scene(self)
        # create_logo_animation(self)

        logo_scene = LogoScene()
        logo_scene.play_logo_animation()
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

        # TODO: 剪辑、配音


"""
if __name__ == '__main__':
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VolumeIPropositionIII"
    os.system(command_A + command_B)
"""


