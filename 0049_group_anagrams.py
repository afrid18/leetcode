class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for i in strs:
            j = i
            temp = "".join(sorted(i))
            if temp in res:
                res[temp].append(j)
            else:
                res[temp] = list()
                res[temp].append(j)
        ans = list()
        for i in res:
            ans.append(res[i])
        return ans
