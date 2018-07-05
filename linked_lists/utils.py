class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next
