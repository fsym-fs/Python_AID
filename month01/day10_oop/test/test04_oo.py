"""
    静态方法
        可以独立存在的工具函数
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, y, x):
        self.x = x
        self.y = y

    @staticmethod
    def get_right():
        """
            静态方法
        """
        return Vector2(0, 1)

    @staticmethod
    def get_up():
        return Vector2(-1, 0)

    @staticmethod
    def get_left():
        return Vector2(0, -1)


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]

# 当前位置
pos = Vector2(1, 2)
# 向右移动
right = Vector2.get_right()
# 需求：沿着某个方向移动
pos.x += right.x
pos.y += right.y

# print(pos.x,pos.y)
# 向左移动
left = Vector2.get_left()
pos.x += left.x
pos.y += left.y
print(pos.x, pos.y)
# 向上移动
up = Vector2.get_up()
pos.x += up.x
pos.y += up.y
print(pos.x, pos.y)

