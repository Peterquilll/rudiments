class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

    def __str__(self):
        return str (self.data)


def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next

def list_str(head):
    if not head:
        return 'x'
    if not head.next:
        return '%s|%s' % (str(head), str(head.random or ''))
    return '%s|%s -> ' % (str(head), str(head.random or '')) \
        + list_str(head.next)
