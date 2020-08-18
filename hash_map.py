# Course: CS261 - Data Structures
# Assignment: 5 Hash Map
# Student: Max Lind
# Description: Hash Map implementation

from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def get_index(self, hash_func, key):
        """
        Helper method to return correct index based on key
        """
        # hash key
        hash = hash_func(key)

        # find correct index based on table capacity
        index = hash % self.capacity

        return index

    def clear(self) -> None:
        """
        Clears content of hash map, does not change capacity
        """
        # loop through table indices
        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            # remove every node in linked list and decrement size
            for node in bucket:
                node.key = None
                node.value = None
                self.size -= 1

        return

    def get(self, key: str) -> object:
        """
        Returns value associated with key
        """
        # get index
        index = self.get_index(self.hash_function, key)

        # get bucket associated with index
        bucket = self.buckets.get_at_index(index)

        # if bucket contains key, return value from that key
        if bucket.contains(key):
            return bucket.contains(key).value

        return None

    def put(self, key: str, value: object) -> None:
        """
        Updates key/value pair in hash map. If key already exists, value is replaced, if not the key/value pair is added. 
        """
        # get correct index based on key
        index = self.get_index(self.hash_function, key)

        # get correct bucket
        bucket = self.buckets.get_at_index(index)

        # if bucket contains key already, remove the key value pair associated with it
        if bucket.contains(key):
            bucket.remove(key)
            self.size -= 1

        # insert new key value pair
        bucket.insert(key, value)

        # increment size
        self.size += 1

        return

    def remove(self, key: str) -> None:
        """
        Removes the given key and its value from the hash map
        """
        # get index
        index = self.get_index(self.hash_function, key)

        # find bucket
        bucket = self.buckets.get_at_index(index)

        # if bucket contains key, remove key value pair and decrement size
        if bucket.contains(key):
            bucket.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if given key is in hash map, otherwise return False
        """
        # get index
        index = self.get_index(self.hash_function, key)

        # get bucket
        bucket = self.buckets.get_at_index(index)

        # if bucket contains key, return True
        if bucket.contains(key):
            return True

        return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table
        """
        empty_buckets = 0

        # loop through dynamic array and check which indices are empty
        for i in range(self.buckets.length()):
            bucket = self.buckets.get_at_index(i)
            if bucket.length() == 0:
                empty_buckets += 1

        return empty_buckets

    def table_load(self) -> float:
        """
        Return table load value
        """
        # table load = number of elements / capacity of array
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes capacity of internal hash table
        """
        # check that capacity can be changed
        if new_capacity < 1:
            return

        # create new hash map
        new_hash = HashMap(new_capacity, self.hash_function)

        # put every node from old buckets into new buckets
        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            for node in bucket:
                new_hash.put(node.key, node.value)

        # update capacity
        self.capacity = new_capacity

        # set new buckets to old buckets
        self.buckets = new_hash.buckets

        return

    def get_keys(self) -> DynamicArray:
        """
        Returns a Dynamic Array that contains all keys from hash map
        """
        # create new dynamic array to return
        key_array = DynamicArray()

        # loop through all buckets
        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)

            # for each node in bucket, append to key array
            for node in bucket:
                key_array.append(node.key)

        return key_array


# BASIC TESTING
# if __name__ == "__main__":

#     print("\nPDF - empty_buckets example 1")
#     print("-----------------------------")
#     m = HashMap(100, hash_function_2)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key1', 10)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key2', 20)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key1', 30)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key4', 40)
#     print(m.empty_buckets(), m.size, m.capacity)

#     print("\nPDF - empty_buckets example 2")
#     print("-----------------------------")
#     m = HashMap(50, hash_function_1)
#     for i in range(150):
#         m.put('key' + str(i), i * 100)
#         if i % 30 == 0:
#             print(m.empty_buckets(), m.size, m.capacity)
#         print(m.empty_buckets())

#     print("\nPDF - table_load example 1")
#     print("--------------------------")
#     m = HashMap(100, hash_function_2)
#     print(m.table_load())
#     m.put('key1', 10)
#     print(m.table_load())
#     m.put('key2', 20)
#     print(m.table_load())
#     m.put('key1', 30)
#     print(m.table_load())

#     print("\nPDF - table_load example 2")
#     print("--------------------------")
#     m = HashMap(50, hash_function_2)
#     for i in range(50):
#         m.put('key' + str(i), i * 100)
#         if i % 10 == 0:
#             print(m.table_load(), m.size, m.capacity)

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)

    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # # print(m.put('str1', 1500))
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))

    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)

    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))

    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')

    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)

    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)

    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')

    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())

    # m.resize_table(1)
    # print(m.get_keys())

    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())
