#LIST
# to indicate the last k values in a list , we use list[-k:]
# to indicate the first k value in a list , we use list[:-k]
# if you wanna merge these to " list[:] = list[-k:] + list[:-k] "

#PRINT
# to include a variable in a print function we use
# print(f"text you want to write {the variable name}")
# print("{} {}".format("value of i is ", i))

#SORTING
# to sort a list including integers or floats 
# we use list.sort(reverse=True) for decreasing list
# we use list.sort() for non-decreasing ones

#CALCULATING
# to round a float to an integer // rounds the float to the nearest integer
# instance : if we say k = 16.20 // 2  , k != 8.20 , k == 8

#CONDITIONS
# to use a for loop in conditon if we use if all(nums[i] <= nums[i + 1] for i in range(lenght - 1))