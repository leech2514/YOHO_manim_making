from manim import *

from common.scenes import play_logo_animation

"""
    命题I.4：边角边（SAS）全等定理。
    若两边及夹角对应相等，则两三角形全等。

    迁移自 _geo/vol1/PropositionI_4.py。
    LogoScene 调用已改为独立函数 play_logo_animation(self)。
"""


class VolumeIPropositionIV(Scene):
    def construct(self):
        # 添加logo动画
        play_logo_animation(self)

        # 标题
        title = Text('第一卷 命题四\n', font_size=50, color=BLUE, font='SimSun')
        title1 = Text("边角边（SAS）全等定理", font_size=40, color=BLUE, font='SimSun')  # 确保标题在顶部

        title_group = VGroup(title, title1)
        title_group.move_to(ORIGIN)
        title_group.shift(UP * 1.2)
        title1.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), runtime=1)
        self.play(Write(title1), runtime=3)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(title1))
        self.wait(1)

        # 创建第一个三角形
        A = np.array([-4, -1, 0])
        B = np.array([-1, -1, 0])
        C = np.array([-2.5, 1, 0])
        triangle1 = Polygon(A, B, C, color=BLUE)
        self.play(FadeIn(triangle1), runtime=1)  # 使用FadeIn

        # 标记第一个三角形的边和角
        label_A = Text("A", font_size=25).next_to(A, DOWN)
        label_B = Text("B", font_size=25).next_to(B, DOWN)
        label_C = Text("C", font_size=25).next_to(C, UP)
        self.play(Write(label_A), Write(label_B), Write(label_C))

        # 创建线段 AB 和 AC
        line_AB = Line(A, B)
        line_AC = Line(A, C)

        # 标记边和角
        side_AB = Text('AB', font_size=25).next_to(line_AB, DOWN)
        side_AC = Text('AC', font_size=25).next_to(line_AC, LEFT)
        angle_A = Angle(line_AB, line_AC, radius=0.5, color=YELLOW)
        self.play(Write(side_AB), Write(side_AC))
        self.wait(1)
        self.play(Write(angle_A))
        self.wait(1)

        # 创建第二个三角形
        D = np.array([2, -1, 0])
        E = np.array([5, -1, 0])
        F = np.array([3.5, 1, 0])
        triangle2 = Polygon(D, E, F, color=GREEN)
        self.play(FadeIn(triangle2))  # 使用FadeIn

        # 标记第二个三角形的边和角
        label_D = Text("D", font_size=25).next_to(D, DOWN)
        label_E = Text("E", font_size=25).next_to(E, DOWN)
        label_F = Text("F", font_size=25).next_to(F, UP)
        self.play(Write(label_D), Write(label_E), Write(label_F))

        # 创建线段 DE 和 DF
        line_DE = Line(D, E)
        line_DF = Line(D, F)

        # 标记边和角
        side_DE = Text('DE', font_size=25).next_to(line_DE, DOWN)
        side_DF = Text('DF', font_size=25).next_to(line_DF, LEFT)
        angle_D = Angle(line_DE, line_DF, radius=0.5, color=YELLOW)
        self.play(Write(side_DE), Write(side_DF), Create(angle_D))


        # 将两个三角形重叠，展示全等
        self.play(
            triangle1.animate.move_to([0, 0, 0]),
            triangle2.animate.move_to([0, 0, 0]),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(label_D), FadeOut(label_E), FadeOut(label_F),
            FadeOut(side_AB), FadeOut(side_AC), FadeOut(side_DE), FadeOut(side_DF),
            FadeOut(angle_A), FadeOut(angle_D),
            run_time=2
        )

        # 显示全等结论
        conclusion = Text("三角形 ABC 和三角形 DEF 全等", color=BLUE, font_size=40)
        conclusion.to_edge(UP)  # 确保结论在顶部
        self.play(Write(conclusion))
        self.wait(2)

        # 证明过程
        proof_texts = [
            "∵ AB = DE, AC = DF, ∠A = ∠D",
            "根据边角边（SAS）全等定理",
            "∴ 三角形 ABC ≅ 三角形 DEF",
            "证完"
        ]

        prev_text = None
        all_texts = []
        for sentence in proof_texts:
            text = Text(sentence, font_size=30)
            if prev_text is None:
                text.shift(LEFT*3 + UP * 2).align_on_border(LEFT)
            else:
                text.next_to(prev_text, DOWN).align_on_border(LEFT)
            self.play(Write(text))
            self.wait(2)
            all_texts.append(text)
            prev_text = text

        self.wait(3)
        self.play(*[FadeOut(text) for text in all_texts])
        self.wait(2)


if __name__ == '__main__':
    scene = VolumeIPropositionIV()
    scene.render()
