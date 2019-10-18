#coding:utf-8
'''
构建二叉树。
二叉树的每个结点包含三个信息：左子结点、右子结点的位置以及自身的值
在建二叉树前，构建结点类。
用队列存储二叉树
队列尾部进，头部出。根结点从头部出时，相应的子结点从尾部进入
'''
# 不同的构建树的
class Binary_tree():
    def __init__(self,val=None,left = None,right = None):
        self.val = val#结点的值
        self.left = left
        self.right = right

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

def build_BST_general(node_list):
    def insert_node(root, node):  # node 待插入的结点
        if root.val >= node.val:
            if root.left is not None:
                insert_node(root.left, node)
            else:
                root.left = node
                return
        # 使用elif而不是if。>= 或者<,只执行其中一种情况。
        # 否则，执行完语句后，还会执行下面的if语句
        elif root.val < node.val:
            if root.right is not None:
                insert_node(root.right, node)
            else:
                root.right = node
                return
    root = node_list[0]

    for node in node_list[1:]:
        insert_node(root, node)
    return root
# node[0].left = node[1]
# node[0].right = node[2]
# node[1].left = node[3]

def level_travelsal(tree,queue):
    current_cursor = tree
    while current_cursor is not None:
        print(current_cursor.val,end=' ')
        if current_cursor.left is not None:
            queue.en_queue(current_cursor.left)
        if current_cursor.right is not None:
            queue.en_queue(current_cursor.right)
        if queue is not None:
            current_cursor = queue.de_queue()
queue = Queue()
l =[2,8,10,4,7,9,3,5]
node_list = [Binary_tree(i) for i in l]#建立结点
root = build_BST_general(node_list)# 建二叉搜索树
level_travelsal(root,queue)

