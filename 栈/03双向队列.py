# coding:utf-8
'''
用python中的列表实现双向队列
双向队列两端均可进列、出列
在这里，将列表的头部看成队列的头部，列表尾看成队列的尾部.这里的定义的方向也可以反过来
'''
class Queue():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self.__list==[]
    def en_front(self,item):
        '''
        头部入列
        :param item:
        :return:
        '''
        self.__list.insert(0,item)
    def en_rear(self,item):
        '''
        尾部入列
        :param item:
        :return:
        '''
        self.__list.append(item)
    def de_front(self):
        '''
        头部出列
        :return:列表头部数据
        '''
        if self.is_empty():
            print('队列已空')
        else:
            return self.__list.pop(0)
    def de_rear(self):
        '''
        尾部部出列
        :return:列表尾部数据
        '''
        if self.is_empty():
            print('队列已空')
        else:
            return self.__list.pop()
    def size(self):
        '''
        :return:栈里面元素个数
        '''
        return len(self.__list)

q = Queue()
q.en_front(2)
q.en_front(3)
q.en_front(4)
q.en_front(5)
print(q.de_rear())
print(q.de_rear())
print(q.de_rear())

print(q.size())