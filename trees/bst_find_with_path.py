from binarytree import build, bst


def find_with_path(root, k, path):
    return []



def main():
    bst_root = bst(height=5)
    k = 6
    path = []
    print('k: ', k)
    print('bst: ', bst_root)

    result = find_with_path(bst_root, k, path)
    print(result)
    
if __name__ == '__main__':
    main()
