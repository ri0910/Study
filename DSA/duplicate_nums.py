from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow
            
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers to check duplicate number, separated by space: ").split()))
    sol = Solution()
    result = sol.findDuplicate(nums)
    print("Duplicate Number is : ", result)
