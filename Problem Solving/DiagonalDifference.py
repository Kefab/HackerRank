import os


def diagonalDifference(arr):
    suma = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i == j):
                suma += arr[i][j]
            if(i+j==(len(arr[i])-1)):
                suma -= arr[i][j]
    return abs(suma)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
