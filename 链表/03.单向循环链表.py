# 单项循环链表，相对于单向链表，链表最后一个结点的next指针指向队首元素
# 判断结束的条件是 last.next == self.__head
class Node(object):
    def __init__(self,item):
        self.element = item
        self.next = None
class Single_cycle_link_list(object):
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node
    def is_empty(self):
        return self.__head == None
    def length(self):
        cursor = self.__head
        if self.is_empty():
            return 0
        count = 1
        while cursor.next != self.__head:# cursor不指向队首，一直计数,指针向后移动
            count += 1
            cursor = cursor.next
        return count
    def insert_head(self,item):#在头部插入,需要找到尾结点的指针
        node = Node(item)
        # 1. 空链表
        if self.is_empty():
            self.__head = node
            node.next = node
        # 2. 非空链表
        else:
            cursor = self.__head
            # 找到队尾结点
            while cursor.next != self.__head:  # 非空
                cursor = cursor.next
            node.next = cursor.next  #
            cursor.next = node
            self.__head = node
    def append(self,item):
        '''
        在尾部插入
        :param item: 待插入的数
        :return: None
        '''
        node = Node(item)

        # 若链表为空，cursor无next属性
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        # 链表不为空,遍历到尾部，尾部指针指向新建的结点，新结点的next指向队首
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        node.next = cursor.next# 新建结点的next指向队首
        cursor.next = node# 队尾的next指向新建结点

    def insert(self,pos,item):
        '''

        :param pos: 插入位置
        :param item: 插入元素
        :return: None
        '''
        if pos < 1:# 位置<1,从头部插入
            self.insert_head(item)
            return
        if pos >= self.length():
            self.append(item)
            return
        node = Node(item)
        count = 0
        pre = None
        cursor = self.__head
        while count < pos:
            # 还没找到时，指针一直向后移动
            pre = cursor
            cursor = cursor.next
            count += 1
        # 找到位置后，改变node指针指向
        node.next = cursor
        pre.next = node

    def remove(self,item):
        '''
        删除元素
        :param item:
        :return:
        '''

        if self.is_empty():
            #空链表
            return
        # 需要有前后指针，pre.next = cursor
        pre = None
        cursor = self.__head

        while cursor.next != self.__head:
            if cursor.element == item:# 找到了待删除的元素
                if pre:
                    pre.next = cursor.next# 删除的不是头结点
                else:# 删掉的是头结点,还需考虑循环过来的情况
                    rear = self.__head# 记录最后一个节点的位置
                    while rear.next != self.__head:
                        rear = rear.next
                    rear.next = cursor.next
                    self.__head = cursor.next
                return
            else:# 没找到，向后移动指针
                pre = cursor
                cursor = cursor.next
        if cursor.element == item: #最后一个元素
            if pre:# 链表中不止一个元素
                pre.next = self.__head
            else: #链表中只有一个元素
                self.__head = None

        #　最后一个元素没考虑进去
        # if cursor.element == item:  # 找到了待删除的元素
        #     if pre:  # 删除的不是头结点
        #         pre.next = cursor.next
        #     else:  # 删掉的是头结点
        #         self.__head = None
        #     return
        # while cursor.next != None:# 最后元素不能在这判断
        #     # 常规情况
        #     if cursor.element == item:
        #         if pre:# 删除的不是头结点
        #             pre.next = cursor.next
        #         else:# 删掉的是头结点
        #             self.__head = cursor.next
        #         return
        #     else:
        #         pre = cursor
        #         cursor = cursor.next
        # if cursor.element == item:# 最后一个元素的情况
        #     if pre:  # 删除的不是头结点
        #         pre.next = cursor.next
        #     else:  # 单个节点的情况
        #         self.__head = cursor.next
    def search(self,item):
        if self.is_empty():
            return False
        cursor = self.__head
        while cursor.next != self.__head:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        if cursor.element == item:
            return True
        return False

    def travel(self):
        '''
        遍历链表，输出
        :return: None
        '''
        if self.is_empty():
            return
        cursor = self.__head
        while cursor.next != self.__head:
            print(cursor.element,end=' ')
            cursor = cursor.next
        print(cursor.element)# 输出最后一个元素


sl = Single_cycle_link_list()
# print('是否是空链表：',sl.is_empty())
# print('链表长度：',sl.length())
# # sl.insert_head(10)
# # sl.insert_head(20)
# # sl.insert_head(30)
# # sl.insert_head(40)
# print('*'*10,' insert_head后 ','*'*10)
# # print('是否是空链表：',sl.is_empty())
# # print('链表长度：',sl.length())
# sl.travel()
#
sl.append(60)
sl.append(70)
sl.append(80)
sl.append(90)
# print('*'*10,' append后 ','*'*10)
# sl.travel()
sl.insert(1,10)
print('*'*10,' insert ','*'*10)
sl.travel()
sl.remove(10)
print('*'*10,' remove ','*'*10)
sl.travel()
print('*'*10,' search ','*'*10)
print('查询结果：',sl.search(60))
