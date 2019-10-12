class Node(object):
    '''
    双向链表，每个节点有一个前驱指针，一个后继指针，一个元素区
    '''
    def __init__(self,item):
        self.element = item
        self.next = None
        self.pre = None
class Bidirection_link_list(object):
    def __init__(self,node=None):
        self.__head = node
    def is_empty(self):
        return self.__head == None
    def length(self):
        cursor = self.__head
        count = 0
        while cursor != None:# cursor不为None，一直计数,指针向后移动
            count += 1
            cursor = cursor.next
        return count
    def insert_head(self,item):#在头部插入
        node = Node(item)
        if self.is_empty():
            self.__head = node
            if node:
                node.next = node
        else:
            node.next = self.__head
            self.__head.pre = node
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
            return
        # 链表不为空,遍历到尾部，尾部指针指向新建的节点
        cursor = self.__head
        while cursor.next != None:
            cursor = cursor.next
        cursor.next = node # 指向后面
        node.pre = cursor # 指向前面
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
        # pre = None# 不需要pre
        cursor = self.__head
        while count < pos:
            count += 1
            cursor = cursor.next

        node.next = cursor
        node.pre = cursor.pre
        cursor.pre.next = node
        cursor.pre = node


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
        cursor = self.__head
        while cursor.next != None:
            if cursor.element == item:
                if cursor.pre:# 删除的不是头结点
                   cursor.pre.next = cursor.next
                   cursor.next.pre = cursor.pre
                else:#删除的是头结点
                    self.__head = cursor.next
                    self.__head.pre = None

                return
            else:
                cursor = cursor.next
        if cursor.element == item:
            cursor.pre.next = None
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
        while cursor != None:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        return False

    def travel(self):
        '''
        遍历链表，输出
        :return: None
        '''
        # if self.is_empty():
        #     return
        cursor = self.__head
        while cursor != None:
            print(cursor.element,end=' ')
            cursor = cursor.next
        print()

sl = Bidirection_link_list()
print('是否是空链表：',sl.is_empty())
print('链表长度：',sl.length())
sl.insert_head(10)
# sl.insert_head(20)
# sl.insert_head(30)
# sl.insert_head(40)
print('*'*10,' insert_head后 ','*'*10)
print('是否是空链表：',sl.is_empty())
print('链表长度：',sl.length())
sl.travel()

sl.append(60)
sl.append(70)
sl.append(80)
sl.append(90)
print('*'*10,' append后 ','*'*10)
sl.travel()
sl.insert(3,'*')
print('*'*10,' insert ','*'*10)
sl.travel()
sl.remove(90)
print('*'*10,' remove ','*'*10)
sl.travel()
print('*'*10,' search ','*'*10)
print('查询结果：',sl.search(80))
