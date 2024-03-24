#print("{} {}".format("firstbracket ",secondbracket ))
#print(f"text {valuable}")

def rotate(nums,k):
    for i in range(k):
        temp=0
        temp=nums[0]
        for j in range(len(nums)-1):
            nums[j]=nums[j+1]
        
        nums[len(nums)-1] =temp
    print(nums)

list = [1,2,3,4,5,6,7]
key = 3
rotate(list,key)







