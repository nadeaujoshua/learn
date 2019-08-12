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


def _selection_sort_alt(a_list):
    """Sort by looking for i-th smallest values."""
    length = len(a_list)
    destination = 0
    while destination < length:
        min_ = destination
        i = destination + 1
        while i < length:
            if a_list[i] < a_list[min_]:
                min_ = i
            i += 1
        a_list[destination], a_list[min_] = a_list[min_], a_list[destination]
        destination += 1


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


def _merge_sort(a_list):
    """Sort an unsorted Python list recursively using merge sort."""
    length = len(a_list)
    if len(a_list) == 1:
        return a_list
    else:
        middle = length // 2
        a = _merge_sort(a_list[:middle])
        b = _merge_sort(a_list[middle:])
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                a_list[k] = a[i]
                i += 1
            else:
                a_list[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            a_list[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            a_list[k] = b[j]
            j += 1
            k += 1
        return a_list
