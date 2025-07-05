x="A2345AA23AAAmnoAwertAAA AAAAAAA 1234AA"
count=0
last=' '
for i in x:
    if i=='A' and last!='A':
        count+=1
    last=i
print(count)

    