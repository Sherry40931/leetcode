import re


def main(pwd: str):
    if re.search('[a-z]', pwd) is None:
        pwd += 'a'
    if re.search('[A-Z]', pwd) is None:
        pwd += 'A'
    if re.search('[0-9]', pwd) is None:
        pwd += '0'
    if re.search('[#@*&]', pwd) is None:
        pwd += '#'

    n = len(pwd)
    if n < 7:
        pwd += 'a' * (7 - n)
    return pwd


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        pwd = input()
        ans = main(pwd)
        print(f'Case #{i+1}: {ans}')

# print(main('1234567'))
# print(main('1111234567'))
# print(main('abcd123'))
# print(main('aA3!'))