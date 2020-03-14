"""
    自定义range(整数生成器)类
"""


# class MyRange_iterator:
#     def __init__(self, start=0, end=0, step=1):
#         self.end = end
#         self.start = start-step
#         self.step = step
#
#     def __next__(self):
#         self.start += self.step
#         if self.start > self.end - 1:
#             raise StopIteration
#         return self.start


class MyRange:
    def __init__(self,end=0):
        self.__end = end

    def __iter__(self):
        # return MyRange_iterator(self.__start, self.__end, self.__step)
        start = 0
        while start < self.__end:
            yield start
            start +=1
        # for i in range(self.__end):
        #     yield i

for item in MyRange(5):
    print(item)
