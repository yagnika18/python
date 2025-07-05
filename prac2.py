n=3
magic_sq=[[0,0,0],
        [0,0,0],
        [0,0,0]]
row=0
col=n//2
num=1
while num<=n*n:
    magic_sq[row][col]=num
    new_row=(row-1)%n
    new_col=(col+1)%n
    if magic_sq[new_row][new_col]!=0:
        row=(row+1)%n
    else:
        row=new_row
        col=new_col
    num+=1
for row in magic_sq:
    print(row)
