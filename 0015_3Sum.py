class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        hs = set()

        lst = list()

        for i in range(len(nums) - 1):
            target = nums[i]
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while(j < k):
                if(nums[j] + nums[k] + target == 0):
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()

                    if tuple(temp) not in hs:
                        lst.append(temp)
                        hs.add(tuple(temp))

                    j += 1
                    k -= 1
                elif(nums[j] + nums[k] + target > 0):
                    k -= 1
                elif(nums[j] + nums[k] + target < 0):
                    j += 1
        return lst
