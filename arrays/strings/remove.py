int_array =[1,2,2,3,4,5,2]
val = int(input("removing number :"))
k = 0 
i=0
while i<len(int_array):
    if int_array[i] == val:
        del int_array[i]

    else:
        k+=1
        i+=1
    
        

for j in range(0,len(int_array),1):
    print(int_array[j])