class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        steps[1] = 1

        if n > 1 :
            steps[2] = 2  # 1+1 / 2 => 2 ways

        if n > 2:
            for i in range(3,n+1):
                steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n]

print(Solution.climbStairs(Solution,3))