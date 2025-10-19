from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_pro = 0
        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i])
            max_pro = max(max_pro, prices[i] - min_price)
        return max_pro

if __name__ == '__main__':
    prices = list(map(int, input("Enter prices with separated spaces: ").split()))

    sol = Solution()
    result = sol.maxProfit(prices)
    print("Max profit will be : ", result)