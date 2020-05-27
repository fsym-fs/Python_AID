"""
创建单链表的数据结构：
1、节点类 - 数据区、链接区
2、单链表类(数学模型): 增加、删除... ...
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """单链表类"""

    def __init__(self, node=None):
        """创建链表时: s=SingleLinkList()表示空链表,s=SingleLinkList(Node(100)) 表示有1个节点的单链表"""
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def lengh(self):
        """获取链表长度"""
        # 游标：从头节点开始,一直往后移动,移动一次,+1
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def travel(self):
        """遍历整个链表"""
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        # 因为上面是end=" ",所以此处打印一个换行
        print()

    def add(self, item):
        """链表头部添加1个节点"""
        node = Node(item)
        # 1、把新添加的节点指针指向原来头节点
        node.next = self.head
        # 2、添加的节点设置为新的头
        self.head = node

    def append(self, item):
        """链表尾部添加1个节点,考虑空链表特殊情况"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            # 循环结束后,current指向尾节点
            current.next = node
            node.next = None

    def search(self, item):
        """查看在链表中是否存在"""
        current = self.head
        while current != None:
            if current.value == item:
                return True
            else:
                current = current.next

        return False

    def insert(self, pos, item):
        """在指定索引添加一个节点,索引值从0开始"""
        if pos < 0:
            self.add(item)
        elif pos > self.lengh() - 1:
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 循环结束后,pos指向(pos-1)位置
            node = Node(item)
            node.next = pre.next
            pre.next = node


if __name__ == '__main__':
    s = SingleLinkList()
    print(s.head)
    # 终端1：True
    print(s.is_empty())
    # 链表：Node(100) -> Node(200) -> Node(300)
    print('1', s.head)
    s.add(200)
    print('2', s.head, s.head.next)
    s.add(100)
    print('3', s.head, s.head.next)
    s.append(300)
    # 终端2：3
    print('4',s.head,s.head.next)
    print(s.lengh())
    # 终端3：100 200 300
    s.travel()
    # 100 666 200 300
    s.insert(1, 666)
    # 终端4: 100 666 200 300
    s.travel()
    # 终端5: True
    print(s.search(666))
