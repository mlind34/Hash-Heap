# Course: CS261 - Data Structures
# Assignment: 5 MinHeap
# Student: Max Lind
# Description: Python implementation of min heap

from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MinHeap with initial values
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Returns MinHeap contents in radable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to MinHeap while maintaining heap property
        """
        # add node to end of array
        self.heap.append(node)

        # find index where node was inserted
        end = self.heap.length() - 1

        # find parent index
        parent = (end - 1) // 2

        # while the value at the parent index is greater than the value and parent index is
        #  not less than 0, swap nodes, set new end index to parent index and find new parent
        while self.heap.get_at_index(parent) > node and parent >= 0:
            self.heap.swap(parent, end)
            end = parent
            parent = (end - 1) // 2
        return

    def get_min(self) -> object:
        """
        Returns object with minimum key without removing it
        """
        if not self.is_empty():
            return self.heap.get_at_index(0)
        else:
            raise MinHeapException

    def find_replacement(self, left_i, right_i, left_child, right_child, replace_val):
        """Returns index position of correct node to be replaced"""
        # if left or right index is out of range, return False
        if left_i > self.heap.length() or right_i > self.heap.length():
            return False

        if left_child is not None and right_child is None:
            if left_child <= replace_val:
                return left_i

        if right_child is not None and left_child is None:
            if right_child <= replace_val:
                return right_i

        if left_child is not None and right_child is not None:
            if left_child <= replace_val and left_child <= right_child:
                return left_i

            if right_child <= replace_val and right_child <= left_child:
                return right_i

    def remove_min(self) -> object:
        """
        Returns object with minimum key and removes it, if empty exception is raised
        """
        if self.is_empty() == True:
            raise MinHeapException

        # minimum value to be returned
        min_val = self.get_min()

        # get last index
        end = self.heap.length() - 1

        # root index
        root = 0

        # swap first and last nodes and remove last value
        self.heap.swap(root, end)
        self.heap.pop()

        # length
        length = self.heap.length()

        # left index and right index
        left_i = (2 * root) + 1
        right_i = (2 * root) + 2

        # if heap has only one value
        if left_i > length - 1:
            return min_val

        # if heap has only left child
        if right_i > length - 1:
            if self.heap.get_at_index(left_i) < self.heap.get_at_index(root):
                self.heap.swap(left_i, root)
                return min_val
            else:
                return min_val

        # percolate down heap
        while left_i < length and right_i < length:
            replace_val = self.heap.get_at_index(root)
            left_child = self.heap.get_at_index(left_i)
            right_child = self.heap.get_at_index(right_i)

            # find index to swap nodes and check that a node exists
            if self.find_replacement(left_i, right_i, left_child, right_child, replace_val):
                node = self.find_replacement(
                    left_i, right_i, left_child, right_child, replace_val)

                # swap nodes, set new root and child indices
                self.heap.swap(root, node)
                root = node
                left_i = (node * 2) + 1
                right_i = (node * 2) + 2

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a proper MinHeap from Dynamic Array
        """
        # clear current content
        for _ in range(self.heap.length()):
            self.heap.pop()

        # create copy array
        for i in range(da.length()):
            self.heap.append(da.get_at_index(i))

        # arr = copy array
        arr = self.heap

        # get first non leaf element and save index
        end = arr.length() - 1

        # parent of first non leaf element to work back in heap
        track_index = (end - 1) // 2

        while track_index >= 0:
            # value at tracking index
            value = arr.get_at_index(track_index)

            # child indices/nodes
            left_i = (2 * track_index) + 1
            right_i = (2 * track_index) + 2
            left_child = arr.get_at_index(left_i)
            right_child = arr.get_at_index(right_i)

            # index to percolate down
            index = track_index

            # while there is a replacement node
            while self.find_replacement(left_i, right_i, left_child, right_child, value):
                node = self.find_replacement(
                    left_i, right_i, left_child, right_child, value)

                # swap nodes, set new parent/child indices
                arr.swap(node, index)
                index = node
                left_i = (node * 2) + 1
                right_i = (node * 2) + 2

            # decrement track index
            track_index -= 1

        return


# BASIC TESTING
# if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # test = [1, 40, 25, 15, 12, 10, 8, 7, 6, 56]
    # for value in test:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap([])
    # print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([40, 15, 15, 15, 15])
    # h2 = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())

    # h = MinHeap([8, 12, 19, 20, 15, 32, 25])
    # print(h.remove_min())
    # print('test')

    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([32, 12, 2, 8, 16, 20, 24, 40, 4, 10, 9])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
