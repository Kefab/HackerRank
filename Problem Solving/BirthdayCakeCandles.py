import os

def birthdayCakeCandles(candles):
    candles.sort()
    candles.reverse()
    tallest = candles[0]
    numberOfTallest = 0
    for i in range(len(candles)):
        if(candles[i] == tallest):
            numberOfTallest+=1
    return numberOfTallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
