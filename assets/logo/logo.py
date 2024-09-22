from manim import *
"""
视频开头的 logo 动画效果
"""
class LogoScene(Scene):
    def construct(self):
        # 创建渐变背景
        background: Rectangle = Rectangle(width=config.frame_width, height=config.frame_height).set_fill(WHITE, opacity=1)
        self.add(background)

        geometry_text: Text = Text("《几何原本》", font_size=80, weight=BOLD)
        geometry_background: RoundedRectangle = RoundedRectangle(corner_radius=0.2, height=geometry_text.height + 0.5, width=geometry_text.width + 0.5, stroke_color=BLACK, stroke_width=4)
        geometry_background.set_fill(BLACK, opacity=0.7)
        geometry_text.move_to(geometry_background.get_center())
        self.play(DrawBorderThenFill(geometry_background))
        self.play(Write(geometry_text))
        self.wait(2)

        # 创建文本 logo
        logo_text: Text = Text("YOHO", font_size=15, weight=BOLD)
        logo_text.set_color(WHITE)  # 设置颜色为白色

        # 添加边框和阴影
        logo_background: RoundedRectangle = RoundedRectangle(corner_radius=0.4, height=logo_text.height + 0.5, width=logo_text.width + 0.5, stroke_color=BLACK, stroke_width=4)
        logo_background.set_fill(BLACK, opacity=0.7)

        # 计算文字大小并设置位置
        logo_background.move_to(1.2 * UP + 2.1 * LEFT)  # 将背景放在左上角
        logo_text.move_to(logo_background.get_center())  # 让文字居中于背景

        # 在场景中显示 logo 和背景
        self.play(DrawBorderThenFill(logo_background))  # 展示背景
        self.play(Write(logo_text))  # 展示文本
        self.wait(2)  # 等待 2 秒以查看效果

        # 添加一个弹出效果
        self.play(logo_text.animate.scale(1.2).set_color(RED), run_time=0.5)
        self.play(logo_text.animate.scale(1/1.1).set_color(BLACK), run_time=0.5)  # 恢复大小

        # 结束场景
        self.play(FadeOut(logo_background), FadeOut(logo_text), FadeOut(geometry_text), runtime=1)

# 要运行该代码，确保使用以下命令：
# manim -pql your_script.py LogoScene