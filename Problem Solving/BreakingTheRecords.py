import os

def breakingRecords(scores):
    a = scores[0]
    b = scores[0]
    maxCount = 0
    minCount = 0
    for score in scores:
        if(score > a):
            maxCount += 1
            a = score
        if(score < b):
            minCount += 1
            b = score
    result = [maxCount,minCount]
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
