def main():
    minp = [min(c), min(m), min(y), min(k)]
    extra = sum(minp) - 10 ** 6
    if extra < 0:
        return 'IMPOSSIBLE'

    i = 0
    while extra > 0:
        rm = min(extra, minp[i])
        minp[i] -= rm
        extra -= rm
        i += 1

    return ' '.join([str(v) for v in minp])


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        c, m, y, k = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        for j in range(3):
            c[j], m[j], y[j], k[j] = [int(v) for v in input().split()]
        ans = main()
        print(f'Case #{i+1}: {ans}')