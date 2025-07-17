class Solution:
  def maximumLength(self, nums: list[int], k: int) -> int:
    dp = [[0] * k for _ in range(k)]
    for x in nums:
      for y in range(k):
        dp[x % k][y] = dp[y][x % k] + 1

    return max(map(max, dp))
