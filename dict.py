# Write a function which returns the sorted list based on "Name". Input data = [('Cricket', 'Dhoni'),('Music', 'ARRehman'),('Scriting', 'Python'),('Singer', 'SPBalu'),('Singer', 'Chitra'),('Singer', 'Jesudas')]
my_dict={"cricket":"Dhoni","music":"Arrehaman","scriting":"Python","Singer":"Chitra","singer":"Jesudas"}
items=list(my_dict.items()) #converts dict to list
for i in range(len(items)):
    for j in range(i+1,len(items)):
        if items[i][1]>items[j][1]:
            items[i],items[j]=items[j],items[i]
for key,value in items:
    print(f" {key}:{value}")




    
    