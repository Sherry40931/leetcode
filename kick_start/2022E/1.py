# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba856a
def main(n: int):
    i = score = 1
    while i < n:
        # John's move
        if n - i >= 3:
            i += 3
        elif n - i >= 2:
            i += 2
        else:
            break

        # bot's move
        if n - i >= 2:
            i += 2
            score += 1
        else:
            break
    return score


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ans = main(n)
        print(f'Case #{i+1}: {ans}')

print(main(1))
print(main(3))
print(main(6))
print(main(4))


# 0 1 2 3 4 5
# r w w r