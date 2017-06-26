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


def has_cycle(head):
    pawn = head
    scout = head

    while scout is not None and scout.next is not None:
        pawn = pawn.next
        scout = scout.next.next
        if pawn == scout:
            return True

    return False


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = forth
    # forth.next = second
     # llist.print_list()

    result = has_cycle(llist.head)
    print(result)