class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique_or_results = set()
        prev = 0
        for index, value in enumerate(arr):
            prev |= value
            current = 0
            for j in range(index, -1, -1):
                current |= arr[j]
                unique_or_results.add(current)
                if current == prev:
                    break
        return len(unique_or_results)
