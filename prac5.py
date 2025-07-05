engineers = ['Saketh', 'Jana', 'Vachan', 'Aura']
programmers = ['Vachan', 'Sama', 'Dheer', 'Aura', 'Achyu']
managers = ['Jana', 'Vachan', 'Dheer', 'Achyu']
list=engineers+programmers+managers
print(list)
new_list=[]
# set=set(Allmix)
# print(set)
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
         
         
         
    

