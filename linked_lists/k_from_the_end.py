from utils import Node, list_str


def k_from_the_end(head, k):
    current = head
    trail = head
    for i in range(k):
        if current is None:
            return None
        current = current.next
    while current is not None:
        trail = trail.next
        current = current.next
    return trail


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    nodes = list(map(Node, data))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    print(list_str(head))

    k = 4
    kth_node = k_from_the_end(head, k)

    print('kth_from_the_end:', kth_node)

if __name__ == "__main__":
    main()
