class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree():
    tree_str = """
            create a tree
              A
            /   |
          B      c
         /\        |
       D   E        F
          /
         G

      前序遍历
      A B D E G C F
      中序遍历
      D B G E A C F
      后序遍历
      D G E B F C A
    """
    print("create tree:\n", tree_str)
    tree = Node("A",
                left=Node("B",
                          left=Node("D", ),
                          right=Node("E", left=Node("G"))),
                right=Node("C",
                           right=Node("F")))
    return tree


if __name__ == '__main__':
    tree = create_tree()
    pass
