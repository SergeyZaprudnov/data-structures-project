"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class Teststack(unittest.TestCase):

    def test_node(self):
        """Тестирование ноды"""
        first = Node(5, None)
        self.assertEqual(first.data, 5)
        self.assertEqual(first.next_node, None)

    def test_queue(self):
        """Тестирование класса Queue"""
        second = Queue()
        three = Queue()
        second.enqueue('data1')
        second.enqueue('data2')
        second.enqueue('data3')
        assert str(second) == "data1\ndata2\ndata3"
        assert str(three) == ""

    def test_dequeue(self):
        four = Queue()
        four.enqueue('data1')
        four.enqueue('data2')
        four.enqueue('data3')

        assert four.dequeue() == 'data1'
        assert four.dequeue() == 'data2'
        assert four.dequeue() == 'data3'
        assert four.dequeue() is None
