phone_no={
    'ram':1234,
    'shyam':3456,
    'mohan':3466
}
print(phone_no)
phone_no['mohan']=9999
phone_no['shyam']={'shyam_home':1215,'shyam_work':2357}
print(phone_no['shyam'])
print(phone_no.get('ram'))
del phone_no['ram']
print(phone_no.pop('shyam'))
print(phone_no)
#popitem=deletes the last item
#.clear=clear all the data
#.keys=return all the keys
#.values=return all the values
#.items=return all the dict iten=ms in the form of tuples
#.copy=copies all the items in old dict to new dict (ex:phone_no2=phone_no.copy)
#.len=gives length of the items