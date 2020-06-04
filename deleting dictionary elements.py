#deleting different dictionary elements:
dict1={}
n=int(input('enter the number of key-value pairs in the dictionary:'))
for i in range(0,n):
    key=input('enter the key:')
    value=input('enter the value:')
    dict1[key]=value
print(dict1)
print('enter the key from the dictionary to be deleted:')
key_del=input()
if(key_del in dict1.keys()):
    del(dict1[key_del])
    print('the entered key has been deleted. the updated dictionary is displayed below:')
    print(dict1)
else:
    print('the key you entered does not exist')
    
