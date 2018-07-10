from utils import Node, print_list

def get_last_r(head):
    if head is None:
        return None
    if head.next is None:
        return head
    return get_last_r(head.next)
    

if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    print_list(head)

    print('\n\n')
    

    result = get_last_r(head)
    print(result)
