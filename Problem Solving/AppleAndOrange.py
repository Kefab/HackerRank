def countApplesAndOranges(s, t, a, b, apples, oranges):
    numOfApple = 0
    numOfOrange = 0
    apples = [apple + a for apple in apples ]
    oranges = [orange + b for orange in oranges]
    for apple in apples:
        if(apple<=t and apple >= s):
            numOfApple+=1
    for orange in oranges:
        if(orange<=t and orange >= s):
            numOfOrange+=1
    print(numOfApple)
    print(numOfOrange)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
