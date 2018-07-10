from utils import Node, print_list

def has_cycle(head):
    current = head
    fast = head

    while current.next and \
          fast and \
          fast.next and \
          fast.next.next:
        current = current.next
        fast = fast.next.next
        if current == fast:
            return True
        
    return False

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
    fifth.next = third

    print('\n\n')

    result = has_cycle(head)
    print(result)
