def main(string: str, n: int, q: int):
    cnt = 0
    s_set = set(string)
    m = len(s_set)
    seen = precalculate(string, n, s_set)

    for _ in range(q):
        i, j = map(int, input().split())
        # check palindrome
        s, e = seen[i - 1], seen[j]
        if sum((s[i] - e[i]) % 2 for i in range(m)) <= 1:
            cnt += 1
    return cnt


def precalculate(string: str, n: int, s_set: set) -> dict:
    occu = {c: 0 for c in s_set}
    seen = [0] * (n + 1)
    seen[0] = tuple(occu.values())
    for i, c in enumerate(string):
        occu[c] += 1
        seen[i + 1] = tuple(occu.values())
    return seen


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, q = map(int, input().split())
        string = input()
        ans = main(string, n, q)
        print(f'Case #{t+1}: {ans}')