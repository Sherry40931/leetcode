import heapq


def main():
    heapq.heapify(dices)
    cnt = 1
    while len(dices) > 0:
        if dices[0] >= cnt:
            cnt += 1
        heapq.heappop(dices)

    return cnt - 1


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        dices = [int(v) for v in input().split()]
        ans = main()
        print(f'Case #{i+1}: {ans}')