def staircase(n):
    for i in range(n):
        for j in range(n - i -1):
            print(' ',end='')
        for _ in range(i+1):
            print("#",end="")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
