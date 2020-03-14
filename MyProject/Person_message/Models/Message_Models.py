"""
    信息产业发展数据是由多条数据记录构成，其信息包括：
        地区、年份、指标名称、计量单位、指标数量等。
        其中，地区包括：全国23个省、4个直辖市、5个自治区和港澳台；
        指标名称包括：固定电话用户数、移动电话用户数、互联网用户数、
        通信固定资产投入、通信业收入、信息服务收入、信息产品收入等。
"""


class Message_Models:
    """
        信息数据模型
    """

    def __init__(self, region_list, year, index_name_list, measuring_unit, index_number):
        self.region_list = region_list
        self.year = year
        self.index_name_list = index_name_list
        self.measuring_unit = measuring_unit
        self.index_number = index_number
