class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre(node):
    print(node.data, end='')
    if node.left != '.':
        pre(tree[node.left])
    if node.right != '.':
        pre(tree[node.right])

def cur(node):
    if node.left != '.':
        cur(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        cur(tree[node.right])

def post(node):
    if node.left != '.':
        post(tree[node.left])
    if node.right != '.':
        post(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = {}

for i in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

pre(tree['A'])
print()
cur(tree['A'])
print()
post(tree['A'])