def bonAppetit(bill, k, b):
    acount = 0
    for i in range(len(bill)):
        if(k != i):
            acount += bill[i]
    acount /= 2
    acount -= b
    if(acount == 0):
        print('Bon Appetit')
    else:
        print(int(abs(acount)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
