class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = 5000
        while(l<=r):
            mid = (l+r)//2
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid - 1
                ans = min(ans, nums[mid])
        return ans
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers to check minimum value in sorted array, separated by space: ").split()))
    sol = Solution()
    res = sol.findMin(nums)
    print("Maximum product of subarray : ", res)