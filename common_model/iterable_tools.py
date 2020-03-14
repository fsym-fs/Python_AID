"""
    可迭代对象的工具
    linq 微软集成查询框架

"""


# 集成操作框架

class IterableHepler:
    """
        可迭代对象助手类
    """

    # 万能按条件升序排序>>>>>sorted()
    @staticmethod
    def sort_up(iterable, func):
        """
        按条件(func)将可迭代对象(iterable)进行升序排序

        :param iterable: 需要搜索的可迭代对象

        :param func:函数类型--->排序条件
        """
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if func(iterable[i]) > func(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]

    # 万能查找满足条件最大的值>>>>>>>max()
    @staticmethod
    def get_max(iterable, func):
        """
        按条件(func)将可迭代对象(iterable)返回最大值

        :param iterable: 需要搜索的可迭代对象

        :param func:函数类型--->条件

        :return:可推算出最大值
        """
        max_item = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_item, iterable[i]):
                max_item = iterable[i]
        return max_item

    # 万能查找自定义内容方法(无条件时)>>>>>map()
    @staticmethod
    def find(iterable, func):
        """
        返回指定内容
        :param iterable: 需要搜索的可迭代对象

        :param func: 函数类型--->需要查找出的内容

        :return: 生成器---->可推算出满足条件的所有对象
        """
        for item in iterable:
            yield func(item)

    # 万能查找所有值方法>>>>>>map()
    @staticmethod
    def find_all(iterable, func_condition):
        """
            根据指定条件(func)在可迭代对象(iterable)中搜索元素

        :param iterable:需要搜索的可迭代对象

        :param func_condition:函数类型---->搜索条件

        :return:生成器---->可推算出满足条件的所有对象
        """
        for item in iterable:
            if func_condition(item):
                yield item

    # 万能查找单一值方法>>>>>>filter()
    @staticmethod
    def find_single(iterable, func_condition):
        """
            根据指定条件(func)在可迭代对象(iterable)中搜索元素

        :param iterable:需要搜索的可迭代对象

        :param func_condition:函数类型---->搜索条件

        :return:生成器---->可推算出满足条件的单个对象
        """
        for item in iterable:
            if func_condition(item):
                return item

    # 按条件删除列表中相同的值
    @staticmethod
    def delete(iterable, func_condition):
        """

        :param iterable:需要搜索的可迭代对象
        :param func_condition:函数类型---->判断条件
        :return:
        """
        for i in range(len(iterable)):
            for j in range(len(iterable) - 1, i, -1):
                if func_condition(iterable[i]) == func_condition(iterable[j]):
                    iterable.remove(iterable[j])
