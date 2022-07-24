import os

def timeConversion(s):
    time = s[len(s)-2:len(s)]
    hour = s[0:len(s)-2]
    times = hour.split(":")
    newTime = ""
    if(time == "AM"):
        if(times[0] == "12"):
            newTime += "00:"
        else:
            newTime += str(times[0]) + ":"
    else:
        if(times[0] == "12"):
            newTime += "12:"
        else:
            newTime += str(int(times[0])+12) + ":"
    newTime+= str(times[1]) + ":"
    newTime+= str(times[2])
    return newTime
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
