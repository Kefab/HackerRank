import os

def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        suma = 0
        for j in range(i,i+m):
            suma += s[j]
        if(suma == d):
            count+=1
    return count
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
