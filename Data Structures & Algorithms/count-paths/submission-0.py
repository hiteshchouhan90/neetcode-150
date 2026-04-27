class Solution:
    def uniquePaths(self, m: int, n: int, memo: dict = None) -> int:
            #Base cases
        if memo is None:
            memo: dict[str, int] = {}
        if m == 1 or n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        key = f"{m},{n}" 
        if key in memo:
            return memo[key]
        memo[key] = self.uniquePaths(m - 1, n, memo ) + self.uniquePaths(m , n - 1, memo)
        return memo[key]