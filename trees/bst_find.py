from binarytree import build, bst


def has_element(root, k):
    if root is None:
        return False
    if root.value == k:
        return True
    if k <= root.value:
        return has_element(root.left, k)
    if k > root.value:
        return has_element(root.right, k)
    



def main():
    bst_root = bst(height=2)
    k = 6
    print('k: ', k)
    print('bst: ', bst_root)

    result = has_element(bst_root, k)
    print(result)
    
if __name__ == '__main__':
    main()
