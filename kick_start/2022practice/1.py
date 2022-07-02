from typing import List


def main(n: int, candies: List[int]):
    return sum(candies) % n


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        _, m = [int(v) for v in input().split()]
        candies = [int(v) for v in input().split()]
        ans = main(m, candies)
        print(f'Case #{i+1}: {ans}')

print(main(3, [1, 2, 3, 4, 5, 6, 7]))
print(main(10, [7, 7, 7, 7, 7]))