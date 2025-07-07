class Solution:
  def maxEvents(self, events: list[list[int]]) -> int:
    ans = 0
    minHeap = []
    i = 0 

    events.sort(key=lambda x: x[0])

    while minHeap or i < len(events):
      if not minHeap:
        d = events[i][0]
      while i < len(events) and events[i][0] == d:
        heapq.heappush(minHeap, events[i][1])
        i += 1
      heapq.heappop(minHeap)
      ans += 1
      d += 1
      while minHeap and minHeap[0] < d:
        heapq.heappop(minHeap)

    return ans
