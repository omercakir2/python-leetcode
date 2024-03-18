class Solution(object):
        def maxProfit(prices):
            maxprof = 0
            lenght = len(prices)
            if all(prices[i] >= prices[i+1] for i in range(lenght-1)):
                maxprof = 0 
                print(maxprof)
            elif all(prices[i] <= prices[i+1] for i in range(lenght-1)):
                maxprof = prices[lenght-1] - prices[0]
                print(maxprof)

            else :
                print(maxprof)

list1 = [1,2,3]
list2 = [3,2,1]
list3 = [1,3,2]
Solution.maxProfit(list1)
Solution.maxProfit(list2)
Solution.maxProfit(list3)