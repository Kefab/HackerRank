import os


def pageCount(n, p):
    book = []
    result = 0
    k = 0
    if(n % 2 != p % 2 and n % 2 == 0):
        n += 1

    for i in range(n+1):
        if(p % 2 == i % 2):
            book.append(i)

    for i in range(len(book)):
        if(book[i] == p):
            result = i
            break

    for i in range(len(book)-1, -1, -1):
        if(book[i] == p and k <= result):
            result = k
            break
        k += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
