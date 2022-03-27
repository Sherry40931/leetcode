def count_I(i_start, j_start):
    cnt = 0
    for i in range(i_start, i_start + half):
        for j in range(j_start, j_start + half):
            if board[i][j] == 'I':
                cnt += 1
    return cnt


def main(N):
    # 0 1
    # 2 3
    cnts = [count_I(0, 0),
            count_I(0, half),
            count_I(half, 0),
            count_I(half, half)]

    # goal: a[2] = a[3], a[1] = a[4]
    return abs(cnts[1] - cnts[2]) + abs(cnts[0] - cnts[3])


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        half = int(input())
        N = half * 2
        board = [[v for v in list(input())] for _ in range(N)]
        ans = main(N)
        print(f'Case #{i+1}: {ans}')