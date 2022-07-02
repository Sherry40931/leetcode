def main(L: int, R: int):
    m = min(L, R)
    return (1 + m) * m // 2


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        L, R = [int(v) for v in input().split()]
        ans = main(L, R)
        print(f'Case #{t+1}: {ans}')


print(main(1, 0))
print(main(1, 1))
print(main(3, 2))
print(main(3, 4))
print(main(5, 4))
print(main(5, 6))

# 1=1-0 ()
# 3=2-0 + 2-1 ()()
# 6 ()()()
# 10 ()()()()