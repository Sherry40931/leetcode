def main(string):
    N = len(string)
    ans, i = '', 0
    while i < N:
        j = i + 1

        while j < N and string[j] == string[i]:
            j += 1

        # increasing
        if j < N and string[i] < string[j]:
            ans += string[i] * (j - i) * 2
        else:
            ans += string[i] * (j - i)

        i = j

    return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        string = input()
        ans = main(string)
        print(f'Case #{i+1}: {ans}')


print(main('PEEL'))
print(main('AAA'))
print(main('CODEJAMDAY'))
print(main('PEEC'))
print(main('ABBBC'))
print(main('CBBBA'))
# PEEEEL
# PEEEL
# PEEL
# PEEC

# ABC -> AABBCC
# AABC
# AABBC

# CBA -> CCBBAA
# CBA