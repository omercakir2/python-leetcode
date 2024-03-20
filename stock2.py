class Solution(object):
        def maxProfit(prices):
            maxprof = 0
            lenght = len(prices)
            if all(prices[i] >= prices[i+1] for i in range(lenght-1)):
                maxprof = 0  # making profit is not possible in this case
                print(maxprof)
            elif all(prices[i] <= prices[i+1] for i in range(lenght-1)):
                maxprof = prices[lenght-1] - prices[0]
                print(maxprof)

            else :
                sell = 0
                buy = 0
                profit = 0
                i = 0
                
                while i < lenght-1:
                    if prices[i+1] > prices[i]:
                        buy = prices[i]
                        for j in range(i,lenght-1,1):
                            if prices[j+1] < prices[j]:
                                sell = prices[j]
                                i = j
                        profit = profit + sell - buy 
                        #print(f"buy  = {buy} , sell = {sell} , profit = {profit} , i = {i}")
                    else : 
                        i +=1
                    print(f"buy  = {buy} , sell = {sell} , profit = {profit} , i = {i-1} ")
                        
                        

                     
                #print(f"max profit {profit}")

       

list1 = [7,1,5,3,6,4]
Solution.maxProfit(list1)
