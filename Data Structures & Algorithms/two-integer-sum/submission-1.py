class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}
        # for index, num in enumerate(nums): 
        #     complement = target - num
        #     if complement in hashmap:
        #         return [hashmap[complement], index]
        #     hashmap[num] = index


        # for index, val in enumerate(nums):
        #     complement = target - val

        #     if complement in hashmap:
        #         return [hashmap[complement], index]
        #     hashmap[val] = index
        
        hash_map = {}
        for index, val in enumerate(nums):
            complement = target - val 
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[val] = index

        return None