from binarytree import convert, pprint


def get_height(node):
    return 0


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = convert(data)

    pprint(root)

    height = get_height(root)

    print('height: ', height)


if __name__ == '__main__':
    main()
