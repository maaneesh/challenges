
# var = {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }

# def flatten_dict(d, parent_key=''):
#     flat_dict ={}
#     for key, value in d.items():
#         new_key = f"{parent_key}.{key}" if parent_key else key
#         if isinstance(value, dict):
#             flat_dict.update(flatten_dict(value, new_key))
#         else:
#             flat_dict[new_key] = value
#     return flat_dict

# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


# ****************************************************************************************************************
# 176
# def isOneToOne(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     dict1 = set(s1)
#     dict2 = set(s2)
#     return len(dict1) == len(dict2)
#
#     # print(flatten_dict(var))
#     print(isOneToOne("foo", "bar"))  # False
#     print(isOneToOne("egg", "add"))  # True
#     print(isOneToOne("abc", "bcd"))  # True
#     print(isOneToOne("ab", "aa"))  # False
#     print(isOneToOne("paper", "title"))  # True
# ****************************************************************************************************************
#  [ 177 ]
# Given a linked list and a positive integer k, rotate the list to the right by k places.
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
# ****************************************************************************************************************
# ****************************************************************************************************************

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete a node from the list."""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def rotate_list(self,k):
        if not self.head or k == 0:
            return self.head
        length = 1
        last = self.head
        while last.next:
            last = last.next
            length += 1
        # rotations needed
        l = k % length
        if l == 0:
            return self.head
        new_tail = self.head
        for _ in range(length - l - 1):
            new_tail = new_tail.next
        # update head and tail pointers
        new_head = new_tail.next
        new_tail.next = None
        last.next = self.head
        self.head = new_head
        return self.head


def main():
    list1 = LinkedList()

    # Add some elements to list1
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)


    list1.display()
    list1.rotate_list(3)
    list1.display()

if __name__ == '__main__':
    main()