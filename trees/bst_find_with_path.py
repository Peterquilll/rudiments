from binarytree import build, bst


def find_with_path(root, k, path):
    if root is None:
        return []
    path.append(root.value)
    if root.value == k:
        return path 
    if k <= root.value:
        return find_with_path(root.left, k, path)
    if k > root.value:
        return find_with_path(root.left, k, path)

    

    
    



def main():
    bst_root = bst(height=3)
    k = 6
    path = []
    print('k: ', k)
    print('bst: ', bst_root)

    result = find_with_path(bst_root, k, path)
    print(result)
    
if __name__ == '__main__':
    main()
