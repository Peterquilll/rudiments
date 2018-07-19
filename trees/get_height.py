from binarytree import build


def get_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    return 1 + max(get_height(root.left),
                   get_height(root.right))


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16]

    root = build(data)

    print(root)

    height = get_height(root)

    print('height: ', height)


if __name__ == '__main__':
    main()
