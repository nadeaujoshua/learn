import pytest

from learn import datastructures


def test_NodeLinkedList():
    n1 = datastructures.NodeLinkedList()
    assert not n1.value
    assert not n1.next

    n2 = datastructures.NodeLinkedList('test')
    n2.next = n1
    assert n2.value == 'test'
    assert n2.next == n1


def test_LinkedList():
    l = datastructures.LinkedList()
    assert not l.head

    l.add('test1')
    assert l.head.value == 'test1'

    l.add('test2')
    assert l.head.value == 'test1'
    assert l.head.next.value == 'test2'
    assert not l.head.next.next

    l.add('test3')
    assert l.linear_search('test3') == 2
    assert l.linear_search('test2') == 1
    assert l.linear_search('test1') == 0
    assert l.linear_search('test4') == -1


def test_MyStack():
    s = datastructures.MyStack()
    assert not s.top

    s.push(1)
    assert s.peek() == 1
    assert s.top.value == 1

    s.push(2)
    assert s.peek() == 2
    assert s.top.value == 2
    assert s.top.next.value == 1
    assert not s.top.next.next

    s.push(3)
    assert s.peek() == 3

    assert s.pop() == 3
    assert s.peek() == 2
    s.pop()
    s.pop()
    assert not s.top


def test_MyQueue():
    q = datastructures.MyQueue()
    assert not q.front
    assert not q.rear
    assert not q.peek()
    assert not q.dequeue()

    q.enqueue(1)
    assert q.front.value == 1
    assert q.rear.value == 1
    assert q.peek() == 1
    assert q.front.value == 1

    assert q.dequeue() == 1
    assert not q.front
    assert not q.rear
    assert not q.peek()
    assert not q.dequeue()

    q.enqueue(2)
    q.enqueue(3)
    assert q.front.value == 2
    assert q.rear.value == 3
    assert q.peek() == 2
    assert q.front.value == 2
    q.enqueue(1)
    assert q.front.value == 2
    assert q.rear.value == 1
    assert q.peek() == 2
    assert q.front.value == 2


def test_MyBinaryTree():
    new_tree = datastructures.MyBinaryTree('a')
    assert new_tree.key == 'a'
    assert new_tree.left_child is None
    assert new_tree.right_child is None

    new_tree.insert_left('b')
    assert new_tree.key == 'a'
    assert new_tree.left_child.key == 'b'
    assert new_tree.left_child.left_child is None
    assert new_tree.right_child is None
    new_tree.insert_left('c')
    assert new_tree.left_child.key == 'c'
    assert new_tree.right_child is None
    assert new_tree.left_child.left_child.key == 'b'
    assert new_tree.left_child.left_child.left_child is None
    assert new_tree.left_child.left_child.right_child is None

    new_tree.insert_right('x')
    assert new_tree.right_child.key == 'x'
    assert new_tree.right_child.left_child is None
    assert new_tree.right_child.right_child is None
    assert new_tree.left_child.key == 'c'
