class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0 
        curr = 0 
        nums = set(nums)

        for s in nums:
            if s - 1 not in nums:
                curr = 1 
                next =  s + 1

                while next in nums:
                    curr += 1
                    next += 1
                best = max(best, curr)
        return best 

        