"""
数学工具函数

合并自原 _2024/v1_Geometry_Fundamentals/utils.py 与 _geo/vol1/utils.py
两版内容完全一致，此处为唯一来源。
"""

import numpy as np


class MathUtils:
    """几何计算工具集合，全部为静态方法，可通过类名直接调用。"""

    @staticmethod
    def distance(x1, y1, x2, y2):
        """
        计算两点 (x1, y1) 与 (x2, y2) 之间的欧氏距离。

        :param x1: 第一个点的 x 坐标
        :param y1: 第一个点的 y 坐标
        :param x2: 第二个点的 x 坐标
        :param y2: 第二个点的 y 坐标
        :return: 两点之间的距离
        """
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    @staticmethod
    def find_intersection_points(A, B, r):
        """
        求两个圆心为 A、B，半径均为 r 的圆的交点。

        :param A: 第一个圆的圆心坐标
        :param B: 第二个圆的圆心坐标
        :param r: 两圆半径（相等）
        :return: 交点列表 [intersection1, intersection2]
        """
        d = np.linalg.norm(B - A)
        a = (r ** 2 - r ** 2 + d ** 2) / (2 * d)
        h = np.sqrt(r ** 2 - a ** 2)
        P2 = A + a * (B - A) / d
        intersection1 = P2 + h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        intersection2 = P2 - h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        return [intersection1, intersection2]

    @staticmethod
    def find_line_circle_intersection(A, B, C, r):
        """
        求线段 AB 与以 C 为圆心、r 为半径的圆的交点。

        :param A: 线段起点
        :param B: 线段终点
        :param C: 圆心
        :param r: 半径
        :return: 交点列表（可能为空、1 个或 2 个）
        """
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
