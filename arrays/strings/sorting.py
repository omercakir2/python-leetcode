# important to know that if all(nums[i] <= nums[i + 1] for i in range(lenght - 1)):
numbers =[2,3,1,5,4,6,54,31,21]
def sort(nums):
    sorted = False
    lenght = len(nums)
    while sorted == False:
        if all(nums[i] <= nums[i + 1] for i in range(lenght - 1)):
            sorted = True

        for i in range(0,lenght-1,1): #bubble sorting method #switching the 2 values evertime
            temp = 0
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp


sort(numbers)
for m in range(0,len(numbers),1):
    print(numbers[m])



