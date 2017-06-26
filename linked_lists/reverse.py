class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        # special 'to string' method
        # defines what should be returned to print() calls
        # on class instances
        return str(self.data)


def list_str(head):
    result = ''
    temp = head
    while temp:
        result += str(temp)
        temp = temp.next
        if temp:
            result += ' -> '

    if not result:
        return 'x'

    return result


def reverse(head):
    """
    Reverse a linked list iteratively
    """
    # add code here
    return head


if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)

    head.next = second
    second.next = third
    third.next = forth

    result = reverse(head)

    print(list_str(result))
