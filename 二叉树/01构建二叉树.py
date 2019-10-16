#coding:utf-8
'''
构建二叉树。
二叉树的每个结点包含三个信息：左子结点、右子结点的位置以及自身的值
在建二叉树前，构建结点类。
用队列存储二叉树
队列尾部进，头部出。根结点从头部出时，相应的子结点从尾部进入
'''
class Node():
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None
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

class Binary_tree():
    def __init__(self):
        self.root = None#根结点
    def add_item(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = Queue()
        current_node = self.root

        while current_node is not None:
            if current_node.left is not None:
                queue.en_queue(current_node.left)
            else:
                current_node.left = node
                return
            if current_node.right is not None:
                queue.en_queue(current_node.right)
            else:
                current_node.right = node
                return
            current_node = queue.de_queue()
    def travel(self):
        if self.root == None:
            return
        current_node = self.root
        queue = Queue()#新建队列，存储待处理的结点。
        # 需要处理的弹出来，如果左右子树存在，将左右子树存储在队列中

        while current_node is not None:# 判断当前结点是否为空
            if current_node.left is not None:
                queue.en_queue(current_node.left)
            if current_node.right is not None:
                queue.en_queue(current_node.right)
            print(current_node.val,end=' ')
            current_node = queue.de_queue()

tree = Binary_tree()
tree.add_item(1)
tree.add_item(2)
tree.add_item(3)
tree.add_item(4)

tree.add_item(5)
tree.add_item(6)
tree.add_item(7)
tree
tree.travel()