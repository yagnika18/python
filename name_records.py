if __name__ == '__main__':
    marks=[]
    name_marks=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append()
        name_marks.append([name,score])
        print(name_marks)
    s=sorted(set(marks))
    second_min=[1]
    for i,j in name_marks:
        if (j== second_min):
            print(i)


        
        