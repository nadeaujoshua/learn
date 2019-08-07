"""Module for implementing sorting algorithms"""

def bubble_sort(linked_list):
    """Sort an instance of LinkedList class using bubble algorithm."""
    switch = False
    current_node = linked_list.head
    while current_node and current_node.next:
        if current_node.value > current_node.next.value:
            switch = True
            temp_value = current_node.next.value
            current_node.next.value = current_node.value
            current_node.value = temp_value
        current_node = current_node.next
        if not current_node.next and switch:
            current_node = linked_list.head
            switch = False


def _selection_sort(a_list):
    """Sort an unsorted Python list in place using selection sort."""
    last = len(a_list) - 1
    while last > 0:
        largest = 0
        i = 1
        while i <= last:
            if a_list[i] > a_list[largest]:
                largest = i
            i += 1
        a_list[largest], a_list[last] = a_list[last], a_list[largest]
        last -= 1


def _insertion_sort(a_list):
    """Sort an unsorted Python list in place using insertion sort."""
    last = len(a_list) - 1
    i = 1
    while i <= last:
        to_sort_val = a_list[i]
        to_place_pos = i
        while to_place_pos and to_sort_val < a_list[to_place_pos-1]:
            a_list[to_place_pos] = a_list[to_place_pos-1]
            to_place_pos -= 1
        a_list[to_place_pos] = to_sort_val
        i += 1
