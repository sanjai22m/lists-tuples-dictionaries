#accessing elments in a tuple:
tup=()
n=int(input('enter the number of elements in the tuple:'))
print('enter the elements:')
for i in range(0,n):
    x=input()
    tup=tup+(x,)
print('enter any number from 1-',n,'to display the elment from the tuple:')
m=int(input())
if(m>0 & m<=n):
    print('the',m,'th element is:',tup[m-1])
print('for slicing, type the ratio of elements to be sliced and printed:')
p=int(input())
q=int(input(':'))
if(p>0 & p<n & q>0 & q<=n):
    print(tup[p:q])
