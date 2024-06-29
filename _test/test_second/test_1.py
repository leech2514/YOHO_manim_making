from manim import *


class PointDefinition(Scene):
    def construct(self):
        # 创建一个点
        point = Dot(color=BLUE)

        # 创建注释文本
        definition_text = Text(
            "点：点不可以再分割成部分。",
            font_size=24
        ).to_edge(UP)

        # 显示点和注释
        self.play(Write(definition_text, run_time=4))
        self.play(FadeIn(point, run_time=2))

        # 强调点的不可分割性
        no_split_text = Text(
            "点不能再分割！",
            font_size=24,
            color=RED
        ).next_to(point, DOWN)

        self.play(Write(no_split_text))

        # 等待一段时间以便观众阅读
        self.wait(2)


# 渲染动画
if __name__ == "__main__":
    from manim import config

    config.media_width = "50%"
    scene = PointDefinition()
    scene.render()
