from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda row:row[1])
        ans = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                ans += 1
            else:
                prev_end = intervals[i][1]
        return ans
    
if __name__ == "__main__":
    n = int(input("Enter number of intervals : "))
    print("Enter intervals (start end) line by line:")
    intervals = [list(map(int, input().split())) for _ in range(n)]
    sol = Solution()
    result = sol.eraseOverlapIntervals(intervals)
    print("Minimum intervals to remove:", result)