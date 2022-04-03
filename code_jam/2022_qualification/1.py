def main():
    for i in range(n_rows):
        for j in range(n_cols):
            if i < 2 and j < 2:
                print('.', end='')
            elif i % 2 == 0 and j % 2 == 0:
                print('+', end='')
            elif i % 2 == 0 and j % 2 == 1:
                print('-', end='')
            elif i % 2 == 1 and j % 2 == 0:
                print('|', end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n_rows, n_cols = [int(v) * 2 + 1 for v in input().split()]
        print(f'Case #{i+1}:')
        ans = main()