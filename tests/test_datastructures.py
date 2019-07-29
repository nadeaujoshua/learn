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
