#assigning elements to different lists:
list1=[]
list2=[]
print('enter the number of elements to be added in list1:')
n=int(input())
print('enter the elements:')
for i in range(0,n):
    x=input()
    list1.append(x)
print('enter the number of elements to be added in list2:')
m=int(input())
print('enter the elements:')
for i in range(0,m):
    y=input()
    list2.append(y)
print('display list 1 or 2 ?')
ans=int(input())
if(ans==1):
    print(list1)
elif(ans==2):
    print(list2)
else:
    print('enter either 1 or 2')
