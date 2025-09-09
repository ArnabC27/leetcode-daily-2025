class Solution:
  def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    MOD = 1_000_000_007
    share = 0
    dp = [0] * n  
    dp[0] = 1

    for i in range(1, n):
      if i - delay >= 0:
        share += dp[i - delay]
      if i - forget >= 0:
        share -= dp[i - forget]
      share += MOD
      share %= MOD
      dp[i] = share

    return sum(dp[-forget:]) % MOD
