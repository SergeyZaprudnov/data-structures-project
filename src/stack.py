class Node:
    """Класс для узла стека"""

    def __init__(self, data, back_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.back_node = back_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data, self.top)
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        node = self.top
        if not node:
            return None
        self.top = node.back_node
        return node.data

    def __str__(self):
        return f'{self.top}'
