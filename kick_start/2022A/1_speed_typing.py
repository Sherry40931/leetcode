def main(I, P):
    if not set(I).issubset(set(P)):
        return 'IMPOSSIBLE'

    ans = 0
    i = j = 0
    M, N = len(I), len(P)
    while i < M and j < N:
        if I[i] == P[j]:
            i, j = i + 1, j + 1
            continue
        while j < N and I[i] != P[j]:
            j += 1
            ans += 1
        if j >= N:
            break

    if i < M:
        return 'IMPOSSIBLE'
    return ans + (N - j)


# if __name__ == '__main__':
#     T = int(input())
#     for i in range(T):
#         I = input()
#         P = input()
#         ans = main(I, P)
#         print(f'Case #{i+1}: {ans}')

print(main('aaaa', 'aaaaa') == 1)
print(main('bbbbb', 'cbbbbc') == 'IMPOSSIBLE')
print(main('Ilovecoding', 'IIllovecoding') == 2)
print(main('KickstartIsFun', 'kkickstartiisfun') == 'IMPOSSIBLE')
print(main('cccccc', 'ceedf') == 'IMPOSSIBLE')
print(main('cc', 'aacccbb') == 5)
print(main('abcd', 'dcba'))