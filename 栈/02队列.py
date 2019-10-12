# coding:utf-8
'''
用python中的列表实现队列
队列是先入先出
在这里，在列表的头部出列，列表尾部入列.这里的定义的方向也可以反过来
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
    def en_queue(self,item):
        '''
        入列
        :param item:
        :return:
        '''
        self.__list.append(item)
    def de_queue(self):
        '''
        出列
        :return:列表头部数据
        '''
        if self.is_empty():
            print('队列已空')
        else:
            return self.__list.pop(0)
    def size(self):
        '''
        :return:栈里面元素个数
        '''
        return len(self.__list)

q = Queue()
q.en_queue(2)
q.en_queue(3)
q.en_queue(4)
q.en_queue(5)
print(q.de_queue())
print(q.de_queue())
print(q.de_queue())

print(q.size())