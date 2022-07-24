import os

def gradingStudents(grades):
    newgrades = []
    for grade in grades:
        if(grade > 37):
            aux = grade
            while(aux%5!=0):
                aux+=1
            if(aux-grade>=3):
                newgrades.append(grade)
            else:
                newgrades.append(aux)
        else:
            newgrades.append(grade)
    return newgrades;
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
