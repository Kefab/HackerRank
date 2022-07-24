import os


def countingValleys(steps, path):
    level = 0
    count = 0
    start = False
    for i in path:
        if(level == 0 and i == 'D'):
            start = True
        elif(start and i == 'U' and level == -1):
            count += 1
        if(i == 'U'):
            level += 1
        else:
            level -= 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
