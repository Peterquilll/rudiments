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
    # you'll need 3 node variables for previous node, current node, and next_node
    # iterate through your list
    #   - then we can do the reversal
    # the final node set to prev is the new head
    # return your new head
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head
    # the three variables was messing me up a bit

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
