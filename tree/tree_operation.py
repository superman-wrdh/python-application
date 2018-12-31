from tree.Tree import create_tree

root_tree = create_tree()


# 层次遍历
def lookup(root):
    row = [root]
    while row:
        print([r.val for r in row])
        row = [kid for item in row for kid in (item.left, item.right) if kid]


# 前序遍历
def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


# 前序遍历
def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)


# 后序遍历
def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)


if __name__ == '__main__':
    print("层次遍历")
    lookup(root_tree)
    print("前序遍历")
    pre_order(root_tree)
    print("中序遍历")
    in_order(root_tree)
    print("后序遍历")
    post_order(root_tree)
