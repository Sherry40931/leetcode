from time import time


def main(string):
    s = 0
    for c in string:
        s += int(c)

    mod = str(9 - (s % 9))
    mod = '0' if mod == '9' else mod

    if mod == '0':
        return string[0] + mod + string[1:]

    max_n = max(string)
    if max_n < mod:
        return string + mod  # add at tail

    N = len(string)
    for i in range(N):
        if i == 0 and mod == '0':
            continue
        if mod < string[i]:
            break

    if i == N - 1 and mod > string[i]:  # add mod at tail
        i += 1

    return string[:i] + mod + string[i:]


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        num = input()
        ans = main(num)
        print(f'Case #{i+1}: {ans}')

print(main('5'))
print(main('33'))
print(main('12121'))
print(main('1456'))
print(main('1654'))
print(main('99'))
print(main('9'))
# a = '1' + ''.join(['0'] * 123455)
# print(main(a))

# 1456 2 -> 12456
# 1654 2 -> 12654