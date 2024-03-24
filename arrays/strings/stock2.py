class Solution(object):
        def maxProfit(prices):
            lenght = len(prices)
            maxprof = 0
            if all(prices[i] >= prices[i+1] for i in range(lenght-1)):
                maxprof = 0  # making profit is not possible in this case
                print(maxprof)
            elif all(prices[i] <= prices[i+1] for i in range(lenght-1)):
                maxprof = prices[lenght-1] - prices[0]
                print(maxprof)

            else :
                sell = 0
                buy = 0
                i = 0
                
                while i < lenght-1:
                    if prices[i+1] > prices[i]:
                        buy = prices[i]
                        if all(prices[k+1]>=prices[k] for k in range(i,lenght-1,1)):
                             sell = prices[lenght-1]
                             maxprof += sell - buy 
                             break
                        for j in range(i,lenght-1,1):
                            if prices[j+1] < prices[j]:
                                 sell = prices[j]
                                 i = j
                                 maxprof += sell - buy
                                 break
                    i += 1
            print(maxprof) 
                            
                     
                 
list1 = [1,9,6,9,1,7,1,1,5,9,9,9]


Solution.maxProfit(list1)
