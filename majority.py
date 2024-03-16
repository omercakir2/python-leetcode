nums =[1,2,1,2,1,2,1,2,1,2,2,2,2,2,1,2]
sums={} #we  need a dictionary to keep that how many copies there are for each value 
for n in nums:
    print("{} {}".format("value of n is ", n))
    if n not in sums:
        sums[n] = 1
    else:
        sums[n] += 1
    if sums[n] > len(nums)//2:
        print("{} {}".format("value of majority is ", sums[n]))
        break

#also another solution for that is below
# return sorted(nums)[len(nums)//2]
    #// rounds the float to the nearest integer