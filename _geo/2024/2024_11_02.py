from manim import *

class RadiusRotationWithTrace(Scene):
    def construct(self):
        # 创建一个圆
        circle = Circle(radius=2)
        self.play(Create(circle))

        # 创建一个点并让它沿着圆的边缘旋转
        point = Dot(color=RED).move_to(circle.point_from_proportion(0))
        self.play(Create(point))

        # 动画参数
        num_rotations = 3
        rotation_angle = 2 * PI * num_rotations
        radius_trace = Line(start=ORIGIN, end=circle.get_center(), color=BLUE)

        # 动态变化半径并留下痕迹
        for i in range(0, 101):
            t = i / 100
            new_radius = 2 * t  # 半径变化
            new_point = circle.point_from_proportion(t)  # 更新点的位置

            # 添加留痕
            if i > 0:
                self.play(Create(Line(prev_point, new_point, color=BLUE)))
            prev_point = new_point

        self.play(FadeOut(point), FadeOut(circle))
