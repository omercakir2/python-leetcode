#we assume that array is non-decreasing order 
nums=[1,1,2,2,3,3,3,3,4,5,6,6,6,6,6,7,7,8,9,10]
i = 0
while i < len(nums)-1:
    if nums[i] != nums[i+1]:
        i+=1
    else:
        del nums[i+1]
        #i+=1
    
for j in range(0,len(nums),1):
    print(nums[j])

    

