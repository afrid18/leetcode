class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            dct[i] = 1 + dct.get(i, 0)
        res = list()
        ans = [[] for i in range(len(nums) + 1)]
        for i, v in dct.items():
            ans[v].append(i)
        final = list()
        for i in range(len(nums), 0, -1):
            for n in ans[i]:
                final.append(n)
                if len(final) == k:
                    return final
