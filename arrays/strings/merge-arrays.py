# range (staring value , stop , step)
# for placeholders , we use .format(valueable you want to place into placeholder) 
# instance :  print("{} {}".format("value of i is ", i))
# append is used to add a new valuable to the list

arrays = []

size = int(input("size of the array you wanna declare"))
for s in range(0,size,1):
    arrays.append(None)


for i in range(0,len(arrays),1):
    arrays[i] = i + 1

for i in range(0,len(arrays),1):
    
    print("{} {}".format("value of i is ", arrays[i]))




