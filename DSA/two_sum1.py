from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if (target - num) in num_map:
                return [num_map[target-num], i]
            num_map[num] = i

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers to check two sum, separated by space: ").split()))
    target = int(input("Enter target : "))

    sol = Solution()
    result = sol.twoSum(nums, target)
    print("Result list : ", result)