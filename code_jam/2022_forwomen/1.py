def count_I(i_start, j_start):
    cnt = 0
    for i in range(i_start, i_start + half):
        for j in range(j_start, j_start + half):
            if board[i][j] == 'I':
                cnt += 1
    return cnt


def main(N):
    cnts = []
    # 0 1
    # 2 3
    cnts.append(count_I(0, 0))
    cnts.append(count_I(0, half))
    cnts.append(count_I(half, 0))
    cnts.append(count_I(half, half))
    # goal: a[2] = a[3], a[1] = a[4]

    ans = abs(cnts[1] - cnts[2]) + abs(cnts[0] - cnts[3])

    return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        half = int(input())
        N = half * 2
        board = [['' for _ in range(N)] for _ in range(N)]
        for k in range(N):
            board[k] = list(input())
        ans = main(N)
        print(f'Case #{i+1}: {ans}')