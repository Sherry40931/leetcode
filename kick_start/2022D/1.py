from statistics import median
from typing import List


def main(m: int, regions: List[int]):
    regions.sort(reverse=True)
    return sum(regions[:m - 1], median(regions[m - 1:]))


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = [int(v) for v in input().split()]
        regions = [int(v) for v in input().split()]
        ans = main(m, regions)
        print(f'Case #{i+1}: {ans}')

print(main(2, [11, 24, 10]))
print(main(1, [6, 2, 5, 1, 9]))