def main(n, x, y, t):
    n_sum = ((1 + n) * n) // 2
    if n_sum % (x + y) != 0:
        print(f'Case #{t}: IMPOSSIBLE')
        return

    x = x * (n_sum // (x + y))
    a = []

    for i in range(n, 0, -1):
        if x >= i:
            x -= i
            a.append(i)

    print(f'Case #{t}: POSSIBLE')
    print(len(a))
    print(*a)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, x, y = [int(v) for v in input().split()]
        main(n, x, y, t + 1)


# main(3, 1, 2, 0)
# main(3, 1, 1, 1)
# main(3, 1, 3, 2)