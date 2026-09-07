"""
场景动画工具

合并自原三份 LogoScene：
  - _2024/v1_Geometry_Fundamentals/utils.py
  - _geo/vol1/utils.py
  - assets/logo/logo.py

设计修正：原 LogoScene.play_logo_animation 同时带 @staticmethod 装饰器与
self 参数，自相矛盾，调用方需写 LogoScene.play_logo_animation(self) 绕过。
现改为独立函数 play_logo_animation(scene)，语义清晰、调用方式直观。
"""

from manim import (
    Scene, Rectangle, RoundedRectangle, Text, VGroup,
    Ellipse, Circle, Dot, Arc, FadeIn,
    WHITE, BLACK, BLUE, RED, BOLD, PINK, GREY,
    DrawBorderThenFill, Write, FadeOut, Create,
    UP, DOWN, LEFT, RIGHT, ORIGIN, DEGREES,
    config,
)


def play_logo_animation(scene: Scene) -> None:
    """
    在传入的场景中播放《几何原本》+ YOHO 的 logo 动画。

    用于每个视频开头。版本 v1.0。

    调用方式（在 Scene.construct 中）：
        from common.scenes import play_logo_animation
        play_logo_animation(self)
    """
    # 背景
    background: Rectangle = Rectangle(
        width=config.frame_width,
        height=config.frame_height,
    ).set_fill(WHITE, opacity=1)
    scene.add(background)

    # 《几何原本》标题
    geometry_text: Text = Text("《几何原本》", font_size=80, weight=BOLD)
    geometry_background = RoundedRectangle(
        corner_radius=0.2,
        height=geometry_text.height + 0.5,
        width=geometry_text.width + 0.5,
        stroke_color=BLACK,
        stroke_width=4,
    )
    geometry_background.set_fill(BLACK, opacity=0.7)
    geometry_text.move_to(geometry_background.get_center())

    scene.play(DrawBorderThenFill(geometry_background))
    scene.play(Write(geometry_text))

    # YOHO 小标
    logo_text: Text = Text("YOHO", font_size=15, weight=BOLD)
    logo_text.set_color(WHITE)

    logo_background: RoundedRectangle = RoundedRectangle(
        corner_radius=0.4,
        height=logo_text.height + 0.5,
        width=logo_text.width + 0.5,
        stroke_color=BLACK,
        stroke_width=4,
    )
    logo_background.set_fill(BLACK, opacity=0.7)
    logo_background.move_to(1.2 * UP + 2.1 * LEFT)
    logo_text.move_to(logo_background.get_center())

    scene.play(DrawBorderThenFill(logo_background))
    scene.play(Write(logo_text))
    scene.wait(1)

    # 弹跳高亮（采用 _geo 版的 BLUE 色）
    scene.play(logo_text.animate.scale(1.2).set_color(BLUE), run_time=0.5)
    scene.play(logo_text.animate.scale(1 / 1.1).set_color(BLACK), run_time=0.5)

    soul2 = VGroup(logo_text, logo_background)
    scene.play(soul2.animate.move_to(1.2 * UP + 2.1 * RIGHT), run_time=0.7)
    scene.play(FadeOut(soul2), run_time=0.5)

    # 收尾
    scene.play(
        FadeOut(background),
        FadeOut(geometry_background),
        FadeOut(geometry_text),
        run_time=1,
    )


def play_rabbit_logo(scene: Scene) -> None:
    """
    在传入的场景中播放一只可爱兔子的 logo 动画。

    兔子造型用 Manim 基本图元（Ellipse / Circle / Dot / Arc）组合而成，
    包含：长耳朵、圆头部、黑眼睛、粉鼻子、微笑嘴、腮红。

    调用方式（在 Scene.construct 中）：
        from common.scenes import play_rabbit_logo
        play_rabbit_logo(self)

    版本 v1.0。
    """
    # 背景
    background = Rectangle(
        width=config.frame_width,
        height=config.frame_height,
    ).set_fill(WHITE, opacity=1)
    scene.add(background)

    # ========== 兔子造型 ==========

    # 耳朵：两只细长椭圆，向外八字分开
    ear_w, ear_h = 0.45, 1.15
    ear_left = Ellipse(width=ear_w, height=ear_h, color=BLACK) \
        .rotate(20 * DEGREES) \
        .move_to(LEFT * 0.55 + UP * 1.8)
    ear_right = Ellipse(width=ear_w, height=ear_h, color=BLACK) \
        .rotate(-20 * DEGREES) \
        .move_to(RIGHT * 0.55 + UP * 1.8)

    # 耳朵内部（粉色），比外轮廓小一圈
    inner_ear_left = Ellipse(width=0.25, height=0.75, color=PINK) \
        .rotate(20 * DEGREES) \
        .move_to(LEFT * 0.55 + UP * 1.8) \
        .set_fill(PINK, opacity=0.9) \
        .set_stroke(PINK, width=0)
    inner_ear_right = Ellipse(width=0.25, height=0.75, color=PINK) \
        .rotate(-20 * DEGREES) \
        .move_to(RIGHT * 0.55 + UP * 1.8) \
        .set_fill(PINK, opacity=0.9) \
        .set_stroke(PINK, width=0)

    # 头部
    head = Circle(radius=1.2, color=BLACK).move_to(ORIGIN)

    # 身体（下方椭圆）
    body = Ellipse(width=1.8, height=1.1, color=BLACK).move_to(DOWN * 1.6)

    # 眼睛：白色蛋形 + 黑色瞳孔
    eye_w, eye_h = 0.28, 0.38
    eye_left = Ellipse(width=eye_w, height=eye_h, color=BLACK) \
        .set_fill(WHITE, opacity=1) \
        .set_stroke(BLACK, width=2) \
        .move_to(LEFT * 0.42 + UP * 0.15)
    eye_right = Ellipse(width=eye_w, height=eye_h, color=BLACK) \
        .set_fill(WHITE, opacity=1) \
        .set_stroke(BLACK, width=2) \
        .move_to(RIGHT * 0.42 + UP * 0.15)
    pupil_left = Dot(radius=0.09, color=BLACK).move_to(LEFT * 0.38 + UP * 0.18)
    pupil_right = Dot(radius=0.09, color=BLACK).move_to(RIGHT * 0.38 + UP * 0.18)

    # 鼻子：粉色小圆
    nose = Dot(radius=0.12, color=PINK).move_to(DOWN * 0.25)

    # 嘴巴：三段弧线（上唇 + 下唇）
    # 上唇中间小 V 形
    mouth_top_left = Arc(
        radius=0.2, start_angle=35 * DEGREES, end_angle=90 * DEGREES,
        color=BLACK, stroke_width=2.5,
    ).move_to(LEFT * 0.1 + DOWN * 0.35)
    mouth_top_right = Arc(
        radius=0.2, start_angle=90 * DEGREES, end_angle=145 * DEGREES,
        color=BLACK, stroke_width=2.5,
    ).move_to(RIGHT * 0.1 + DOWN * 0.35)
    # 下唇微笑
    mouth_bottom = Arc(
        radius=0.45, start_angle=200 * DEGREES, end_angle=340 * DEGREES,
        color=BLACK, stroke_width=2.5,
    ).move_to(DOWN * 0.55)

    # 腮红：两个粉色小圆
    blush_left = Dot(radius=0.18, color=PINK) \
        .set_fill(PINK, opacity=0.6) \
        .move_to(LEFT * 0.72 + DOWN * 0.15)
    blush_right = Dot(radius=0.18, color=PINK) \
        .set_fill(PINK, opacity=0.6) \
        .move_to(RIGHT * 0.72 + DOWN * 0.15)

    # 分组
    bunny_outline = VGroup(ear_left, ear_right, head, body)
    bunny_inner = VGroup(inner_ear_left, inner_ear_right)
    bunny_details = VGroup(
        eye_left, eye_right, pupil_left, pupil_right,
        nose, mouth_top_left, mouth_top_right, mouth_bottom,
        blush_left, blush_right,
    )
    bunny_full = VGroup(bunny_outline, bunny_inner, bunny_details)

    # ========== 动画 ==========

    # 1) 先画外轮廓（耳朵 + 头 + 身体）
    scene.play(DrawBorderThenFill(ear_left), DrawBorderThenFill(ear_right), run_time=0.8)
    scene.play(DrawBorderThenFill(head), run_time=0.8)
    scene.play(DrawBorderThenFill(body), run_time=0.6)

    # 2) 填充耳朵内部粉色
    scene.play(FadeIn(inner_ear_left), FadeIn(inner_ear_right), run_time=0.5)

    # 3) 写入五官细节
    scene.play(Write(eye_left), Write(eye_right), run_time=0.5)
    scene.play(FadeIn(pupil_left), FadeIn(pupil_right), run_time=0.4)
    scene.play(FadeIn(nose), run_time=0.3)
    scene.play(
        Create(mouth_top_left), Create(mouth_top_right),
        Create(mouth_bottom), run_time=0.8,
    )
    scene.play(FadeIn(blush_left), FadeIn(blush_right), run_time=0.4)

    scene.wait(0.5)

    # 4) 弹跳高亮（整体放大 + 耳朵变蓝 + 恢复）
    scene.play(
        bunny_full.animate.scale(1.15),
        ear_left.animate.set_stroke(BLUE, width=6),
        ear_right.animate.set_stroke(BLUE, width=6),
        run_time=0.5,
    )
    scene.play(
        bunny_full.animate.scale(1 / 1.15),
        ear_left.animate.set_stroke(BLACK, width=4),
        ear_right.animate.set_stroke(BLACK, width=4),
        run_time=0.5,
    )

    scene.wait(0.5)

    # 5) 收尾淡出
    scene.play(FadeOut(bunny_full), FadeOut(background), run_time=1)
