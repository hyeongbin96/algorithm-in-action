import math

N = int(input())
tree = []
tree_dist = []

for i in range(N) :
    num = int(input())
    if len(tree) == 0 :
        tree.append(num)
    else :
        tree.append(num)
        tree_dist.append(tree[i] - tree[i-1])

gcd = math.gcd(*tree_dist)

result = (sum(tree_dist) // gcd) - (len(tree_dist))
print(result)