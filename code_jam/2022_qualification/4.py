from collections import defaultdict
from typing import List
from pdb import set_trace as bp


def dfs(graph: dict, fun: List[int]):
    N = len(fun)
    ans = 0
    up = [0] * N  # value pass to parent, which is the max value of current chain

    for node in range(N - 1, 0, -1):
        childs_val = sorted([up[v] for v in graph[node]])

        # pass value to parent
        pass_up = 0
        if len(childs_val) > 0:
            pass_up = childs_val[0]
        up[node] = max(pass_up, fun[node])

        # if have other branch, add to ans
        # 因為不會往上 pass, 這個 chain 得到的值就是目前的 max
        if len(childs_val) > 1:
            ans += sum(childs_val[1:])
        # print(node, childs_val, up, ans)

    # add nodes that point to abyss (root or single node)
    ans += sum([v for i, v in enumerate(up) if i in graph[0]])
    return ans


def main(fun: List[int], points: List[int]):
    fun = [-1] + fun
    points = [-1] + points

    graph = defaultdict(list)
    for i, p in enumerate(points[1:], start=1):
        graph[p].append(i)

    return dfs(graph, fun)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        fun = [int(v) for v in input().split()]
        pointers = [int(v) for v in input().split()]
        ans = main(fun, pointers)
        print(f'Case #{i+1}: {ans}')


print(main([60, 20, 40, 50], [0, 1, 1, 2]))
print(main([3, 2, 1, 4, 5], [0, 1, 1, 1, 0]))
print(main([100, 100, 100, 90, 80, 100, 90, 100], [0, 1, 2, 1, 2, 3, 1, 3]))

# print(main([5, 3, 2, 1, 4], [0, 1, 2, 3, 3]))
# print(main([5, 3, 2, 1, 4], [0, 1, 2, 2, 2]))
# print(main([5, 3, 2, 1, 4], [0, 1, 1, 1, 1]))
# print(main([5, 6, 4, 2, 1], [0, 1, 1, 2, 3]))
# print(main([5, 6, 4, 2, 1], [0, 1, 2, 2, 3]))
# print(main([5, 4, 3, 2, 10, 6], [0, 1, 2, 1, 2, 3]))
# print(main([1, 2], [0, 1]))
# print(main([5, 4, 3, 2, 6, 1], [0, 1, 2, 1, 2, 3]))