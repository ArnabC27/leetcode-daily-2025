class Solution:
    def hammingDistance(self, a: str, b: str) -> int:
        return sum(1 for x, y in zip(a, b) if x != y)

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        lis = [1] * n
        parent = [-1] * n

        lis_len, lis_end = 1, 0
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    groups[i] != groups[j]
                    and len(words[i]) == len(words[j])
                    and self.hammingDistance(words[i], words[j]) == 1
                    and lis[i] + 1 > lis[j]
                ):
                    lis[j] = lis[i] + 1
                    parent[j] = i
                    if lis[j] > lis_len:
                        lis_len = lis[j]
                        lis_end = j

        ans = []
        cur = lis_end
        while cur != -1:
            ans.append(words[cur])
            cur = parent[cur]
        return ans[::-1]
