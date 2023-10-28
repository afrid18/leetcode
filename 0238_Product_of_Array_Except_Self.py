# My solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
                if zeros > 1:
                    break
        if zeros > 1:
            answer = [0] * len(nums)
            return answer
        elif zeros == 1:
            idx = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    idx = i
                    break
            res = 1
            for i in range(len(nums)):
                if i == idx:
                    continue
                else:
                    res *= nums[i]
            answer = [0] * len(nums)
            answer[idx] = res
            return answer
        else:
            for i in range(len(nums)):
                mul *= nums[i]
            answer = [mul] * len(nums)
            for i in range(len(answer)):
                answer[i] //= nums[i]
            return answer

# Neetcode solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)

        # Prefix
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            answer[i] = prefix
        
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            answer[i] *= postfix

        return answer
