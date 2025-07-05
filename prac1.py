# def replace_duplicates(lst,replacement_value):
#     result=[]
#     for i in range(0,len(lst)):
#         is_duplicate=False
#         for j in range(i):
#             if lst[i]==lst[j]:
#               is_duplicate=True
#               break;
#         if is_duplicate:
#             result.append(replacement_value)
#         else:
#             result.append(lst[i])
#     return result
# lst=[1,4,8,2,3,1,5,3,6,8]
# new_list=replace_duplicates(lst,0)
# print (new_list)
# new_list.remove(0)
# print(new_list)
list=[3,6,9,2,3,1,7,2]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            list[j]=0
print(list)
