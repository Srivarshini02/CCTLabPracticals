'''val1=eval(input("list1: "))
val2=eval(input("list2: "))
l1=list(val1)
l2=list(val2)
l3=[]
if(len(l1)==len(l2)):
    for i in range(0,len(l1)):
            fin=abs(l1[i]-l2[i])
            l3.append(fin)
else:
    
print(l3)'''


a=(input("data: "))
t=tuple(a.split(','))

print(t)
