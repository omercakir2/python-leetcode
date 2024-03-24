list1 = [ 1,3,5,6,9,9 ]
list2 = [ 4,4,7,8 ]

n = len(list1)-1 
m = len(list2)-1

for i in range(0,m+1,1):
    list1.append(0)

#last elemen of the final array 
lastoffinal = m+n+1

while m>=0 and n>=0 :
    if list1[n] > list2[m]:
        list1[lastoffinal] = list1[n]
        n -=1
        lastoffinal -=1

    else:
        list1[lastoffinal] = list2[m]
        m -=1
        lastoffinal -=1
    
for i in range(0,len(list1),1):
    print(list1[i])



