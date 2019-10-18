#coding:utf-8
class Binary_tree():
    def __init__(self,val=None,left = None,right = None,flag=0):
        self.val = val#结点的值
        self.left = left
        self.right = right
        self.flag = flag
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
            pass
            # print('队列已空')
        else:
            return self.__list.pop(0)
    def size(self):
        '''
        :return:栈里面元素个数
        '''
        return len(self.__list)

def build_BST_general(node_list):


    def build_BST(root, node):  # node 待插入的结点
        if root.val >= node.val:
            if root.left is not None:
                build_BST(root.left, node)
            else:
                root.left = node
                return
        # 使用elif而不是if。>= 或者<,只执行其中一种情况。
        # 否则，执行完语句后，还会执行下面的if语句
        elif root.val < node.val:
            if root.right is not None:
                build_BST(root.right, node)
            else:
                root.right = node
                return

    root = node_list[0]
    for node in node_list[1:]:
        build_BST(root, node)
    return root

queue = Queue()
def level_travelsal(tree,result):
    current_cursor = tree
    while current_cursor is not None:
        result.append(current_cursor.val)
        # print(current_cursor.val,end=' ')
        if current_cursor.left is not None:
            queue.en_queue(current_cursor.left)
        if current_cursor.right is not None:
            queue.en_queue(current_cursor.right)
        if queue is not None:
            current_cursor = queue.de_queue()


# sample = [3,1,4,2]
# test_list = [[3,4,1,2],[3,2,4,1]]
def main():
    while True:
        first_line = input('请输入N和L:\n')
        # print(first_line)
        first_line = first_line.split()
        if len(first_line)<2:
            break
        N,L = int(first_line[0]),int(first_line[1])
        if not N:
            break
        sample = list(map(int,input('原始序列：\n').split()))
        test_list = []
        for i in range(L):
            temp = list(map(int,input('第{}组测试序列：\n'.format(i+1)).split()))
            test_list.append(temp)

        node_sample = [Binary_tree(i) for i in sample]
        BST_sample = build_BST_general(node_sample)
        travel_sample = []
        level_travelsal(BST_sample,travel_sample)

        for test_sample in test_list:
            node_test = [Binary_tree(i) for i in test_sample]
            BST_test = build_BST_general(node_test)
            travel_test = []
            level_travelsal(BST_test, travel_test)
            if travel_test == travel_sample:
                return True
            else:
                return False

if __name__ == '__main__':
    l = [6,2,8,10,4,7,9,3,5]
    root = build_BST_general(l)
    result = []
    level_travelsal(root,result)
    print(result)

    # main()
