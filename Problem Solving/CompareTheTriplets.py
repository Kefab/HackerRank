import os

def compareTriplets(a, b):
    c = [0,0]
    for i in range(3):
        if(a[i] < b[i]):
            c[1] +=1
        elif(a[i]>b[i]):
            c[0] += 1
    return c
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
