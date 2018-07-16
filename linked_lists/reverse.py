from utils import Node, list_str


def reverse(head):
    current = head
    next_node = head

    next_node = next_node.next
    next_node.next = current
    current.next = None

    return next_node


def main():
    data = [1, 2]#, 3, 4, 5, 6, 7, 8]
    nodes = list(map(Node, data))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    print(list_str(head))

    new_head = reverse(head)

    print('New head:', new_head)
    print(list_str(new_head))
    
if __name__ == "__main__":
    main()
