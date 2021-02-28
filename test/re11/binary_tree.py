def binary_tree(key, tree): return tree[1] if tree[0] == key else binary_tree(key, tree[2]() if key < tree[0] else tree[3]()) # "os one-liners do Miguel" :(
