"""
test08_function
"""


class test08_function:
    """
        关于函数的练习

    """

    def print_grade(self, score):
        """
            获取成绩
            判断等级(优,良,及格,不及格,不在范围内(0-100))

            :param score:float型 -->学生的成绩

            :return:字符型--->返回成绩相应的等级
        """
        score = float(score)
        if score >= 90 and score <= 100:  # 判断在(90-100)是优秀等级
            return "优秀"
        if score >= 80:  # 判断在(80-90)以内是优秀良好
            return "良好"
        if score >= 60:  # 判断在(60-80)以内是及格等级
            return "及格"
        if score < 60 and score >= 0:  # 判断<60是不及格
            return "不及格"
        # 判断不在(0-100)以内是
        return "不在范围内(0-100)"

    def print_add_bits(self, number):
        """
            获取一个任意整数   ---->123456
            输出每位相加的和 ----->1+2+3+4+5+6

            :param number:字符型--->一个任意整数

            :return:int型--->输出每位相加的和
        """
        result = 0
        for i in str(number):  # 获取每一个位
            result += int(i)  # 循环相加每一个位
        return result


f = test08_function()
print(f.print_grade(97))
print(f.print_add_bits(1234))
