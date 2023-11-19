class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        i = 0
        j = len(height) - 1

        while(i < j):
            area = (j - i) * min(height[i], height[j])
            mx = max(area, mx)

            if(height[i] < height[j]):
                i += 1
            elif(height[j] < height[i]):
                j -= 1
            else:
                j -= 1
                i += 1

        return mx

