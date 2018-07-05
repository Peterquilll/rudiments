from utils import Node, print_list

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
    k = 2
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)

    head.next = second
    second.next = third
    third.next = forth
    print_list(head)

    print('\n\n')

    result = nth_to_last(head, k)
    print(result.data)
