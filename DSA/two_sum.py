from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = list()
        d = dict()
        for i in range(len(nums)):
            if (target - nums[i]) not in d:
                d[nums[i]] = i
            else:
                l.append(d[target - nums[i]])
                l.append(i)
        return l


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space : ").split()))
    target = int(input("Enter target value: "))

    sol = Solution()
    output = sol.twoSum(nums, target)
    print("Out put of Two Sum : ", output)
