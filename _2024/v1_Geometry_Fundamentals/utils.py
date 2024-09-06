import numpy as np
"""
This file contains the MathUtils class which contains static methods for mathematical operations.
"""
class MathUtils:
    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    @staticmethod
    def find_intersection_points(A, B, r):
        """
        Find the intersection points of two circles with centers A and B and radius r.
        :param A:
        :param B:
        :param r:
        :return:
        """
        """
        什么是静态方法？如何使用？
        @staticmethods 是一个装饰器，用来定义静态方法。不需要self参数，可以直接通过类名调用。只依赖传入的参数，不依赖于实例的状态。
        1.可直接被调用，不需要实例化对象：如math.sqrt(x)
        """
        # A and B are the centers of the circles
        # r is the radius of the circles
        d = np.linalg.norm(B - A)
        a = (r ** 2 - r ** 2 + d ** 2) / (2 * d)
        h = np.sqrt(r ** 2 - a ** 2)
        P2 = A + a * (B - A) / d
        intersection1 = P2 + h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        intersection2 = P2 - h * np.array([-(B - A)[1], (B - A)[0], 0]) / d
        return [intersection1, intersection2]