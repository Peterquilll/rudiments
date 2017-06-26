class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def nth_to_last(head, k):
    p1 = head
    p2 = head
    for i in range(0, k):
        if p1 is None:
            return None
        p1 = p1.next
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2

if __name__ == '__main__':
    k = int(input("Number: "))
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = forth
    llist.print_list()

    result = nth_to_last(llist.head, k)
    print(result.data)