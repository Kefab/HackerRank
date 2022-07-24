def miniMaxSum(arr):
    arr.sort()
    _max = 0
    _min = 0
    for i in range(1,(len(arr)-1)):
        _max += arr[i]
    _min = _max
    _min += arr[0]
    _max += arr[len(arr)-1]
    print(f"{_min} {_max}" )
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
