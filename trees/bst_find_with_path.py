from binarytree import build, bst


def find_with_path(root, k, path):
    if root is None:
        return False
    if root.value == k:
        return path
    if root.left is None and root.right is None:
        return False
    
    path.append(root.value)
    
    if k <= root.value:
        return find_with_path(root.left, k, path)

    return find_with_path(root.right, k, path)



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
