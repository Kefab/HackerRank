def plusMinus(arr):
    negatives = 0
    positives = 0
    zeros = 0
    for i in arr:
        if(i <0):
            negatives +=1
        elif(i>0):
            positives +=1
        else:
            zeros += 1
    
            
    print('{:.6f}'.format(positives/len(arr)))
    print('{:.6f}'.format(negatives/len(arr)))
    print('{:.6f}'.format(zeros/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
