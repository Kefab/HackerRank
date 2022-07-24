import os

def getTotalX(a, b):
    a.sort()
    b.sort()
    
    multiple = a[len(a)-1]
    multiples = []
    count = 0
    
    while(multiple <= b[0]):
        flag = True
        for i in a:
            if(multiple%i!=0):
                flag = False
        if(flag):
            multiples.append(multiple)
        multiple+=1

    for multiple in multiples:
        flag = True
        for i in b:
            if(i%multiple!=0):
                flag = False
        if(flag):
            count += 1
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
