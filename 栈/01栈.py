# coding:utf-8
'''
用python中的列表实现栈
栈是后入先出
在这里，将列表的尾部看成活动的
入栈和出栈都在列表尾部实现
列表尾部也是栈顶
'''
class Stack():
    def __init__(self):
        self.__list = []
    def is_empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self.__list==[]

    def push(self,item):
        '''
        入栈.
        :param item:压入元素
        :return:
        '''
        self.__list.append(item)
    def pop(self):
        '''
        出栈
        :return: 列表弹出的栈顶元素
        '''
        if self.is_empty():
            print('栈已空')
        else:
            return self.__list.pop()
    def peek(self):
        '''
        读取栈顶元素，不改变原列表
        :return: 栈顶元素
        '''
        return self.__list[-1]

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
print(s.pop())
print(s.pop())

print(s.size())