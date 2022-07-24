import os


def sockMerchant(n, ar):
    uniqueSock = []
    result = 0
    for i in ar:
        if(i not in uniqueSock):
            uniqueSock.append(i)
    for i in uniqueSock:
        numberSock = ar.count(i)
        if(numberSock % 2 == 0):
            result += (numberSock/2)
        else:
            numberSock -= 1
            result += (numberSock/2)
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
