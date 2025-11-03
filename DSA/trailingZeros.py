class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = 0
        while(n > 0):
            r = n//5
            f += r
            n = n//5
        return f
    
if __name__ == "__main__":
    target = int(input("Enter target value: "))

    sol = Solution()
    num = sol.trailingZeroes(target)
    print("Number of trailing zeros : ", num)