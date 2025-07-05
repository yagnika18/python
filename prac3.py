a="  Bad things    happen to   good people   because things     happen and    it's up to     people to    determine what's    good."
b=a.split()
for x in range(len(b)):
    print(b[x])
    b[x]=b[x].capitalize()
    print(b)
c=' '.join(b)
print(c)
