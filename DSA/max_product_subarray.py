from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for num in nums:
            tmp = num * curMax
            curMax = max(num*curMax, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res = max(res, curMax)
        return res
        
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers to check max product of subarray, separated by space: ").split()))
    sol = Solution()
    res = sol.maxProduct(nums)
    print("Maximum product of subarray : ", res)