from manim import *

"""
    执行的命令：manim -p -ql first.py SquareToCircle
    执行时如果出现权限相关的问题，把电脑的安全软件关一下
"""


class SecondExample(Scene):
    def construct(self):
        # 创建坐标系
        ax = Axes(
            x_range=(-3, 3),
            y_range=(-3, 3),
            axis_config={"color": BLUE}  # 设置轴线的颜色为蓝色
        )

        # 在坐标系创建曲线函数
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2), color=RED)

        # 指定x轴的范围
        area = ax.get_area(curve, x_range=(-2, 0))
        # 以动画的形式展示创建过程
        self.play(Create(ax))
        self.play(Create(curve, run_time=6))
        self.play(FadeIn(area, run_time=3))
        self.wait(2)


class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        # 画出图像的边界，并填充颜色
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        # 代替转换
        self.play(ReplacementTransform(green_square, blue_circle, run_time=6))
        # Indicate是让传入的参数对象变大，颜色为黄色。在吸引观众方面挺有用的
        self.play(Indicate(blue_circle, run_time=4))
        # 对象淡出
        self.play(FadeOut(blue_circle, run_time=4))
        self.wait(2)


class CreateAndFillTable(Scene):
    def construct(self):
        # Step 1: Create the table
        table = Table(
            [["", "", ""], ["", "", ""], ["", "", ""]],
            col_labels=[Text("班级"), Text("性别"), Text("分数")],
            row_labels=[Text("小王"), Text("小李"), Text("小张")],
            include_outer_lines=True,
        ).scale(0.75)

        table_name = Text("学生信息表").scale(0.75).next_to(table, UP)

        self.play(Create(table), Write(table_name))
        self.wait(1)

        # Step 2: Fill the table with data
        data = [
            ["1", "女", "66"],
            ["2", "女", "75"],
            ["1", "男", "93"]
        ]

        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                cell_rect = table.get_highlighted_cell((i + 2, j + 2), color=YELLOW)
                self.play(Create(cell_rect))
                self.play(Write(Text(cell).move_to(table.get_cell((i + 2, j + 2)).get_center())))
                self.wait(0.5)
                # Remove the highlight
                self.play(FadeOut(cell_rect))

        self.wait(1)

        # Highlight rows from second to fourth (adjust range accordingly)
        for row_num in range(1, 4):  # Rows 2 to 4 in 1-indexed notation
            row_cells = [table.get_cell((row_num + 1, col)) for col in range(1, 5)]
            row_highlight = SurroundingRectangle(VGroup(*row_cells), color=YELLOW, buff=0.1)
            self.play(Create(row_highlight))
            self.wait(1)
            self.play(FadeOut(row_highlight))

        self.wait(2)


# To render the scene, run the following command in your terminal:
# manim -pql table_example.py CreateAndFillTable




if __name__ == "__main__":
    scene = SecondExample()
    scene.render()
