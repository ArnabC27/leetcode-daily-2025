class Solution:
  def putMarbles(self, weights: list[int], k: int) -> int:
    arr = [a + b for a, b in itertools.pairwise(weights)]
    return sum(heapq.nlargest(k - 1, arr)) - sum(heapq.nsmallest(k - 1, arr))
