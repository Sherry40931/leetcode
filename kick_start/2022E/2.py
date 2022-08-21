# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba84ae
from bisect import bisect_left
from typing import List


def main(n: int, ratings: List[int]):
    mentors = [(v, i) for i, v in sorted(enumerate(ratings), key=lambda x: x[1])]
    ans = [-1] * n
    for i in range(n):
        idx = bisect_left(mentors, (ratings[i] * 2, n + 1)) - 1
        while mentors[idx][1] == i:
            idx -= 1
        if idx >= 0:
            ans[i] = mentors[idx][0]

    return ' '.join([str(v) for v in ans])


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        ratings = [int(v) for v in input().split()]
        ans = main(n, ratings)
        print(f'Case #{t+1}: {ans}')


print(main(3, [2000, 1500, 1900]))
print(main(5, [1000, 600, 1000, 2300, 1800]))
print(main(2, [2500, 1200]))