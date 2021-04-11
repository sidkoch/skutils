
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    list_1 = LinkedList()

    list_1.head = Node(10)
    second = Node(20)
    third = Node(30)

    list_1.head.next = second
    second.next = third

    print("objects in memory - ")
    print(list_1)
    print(list_1.head)
    print(list_1.head.next)
    print(list_1.head.next.next)
    print(list_1.head.next.next.next)
    print("\ndata stored - ")
    print(list_1.head.item)
    print(list_1.head.next.item)
    print(list_1.head.next.next.item)
