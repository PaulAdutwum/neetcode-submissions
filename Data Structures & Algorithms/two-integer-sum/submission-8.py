class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


       # hashmap = {}
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
        
        # hash_map = {}
        # for index, val in enumerate(nums):
        #     complement = target - val 
        #     if complement in hash_map:
        #         return [hash_map[complement], index]
        #     hash_map[val] = index

        # return None

        """
        I will create a hashmap that has vals as keys and indeces
        as values 

        for each val, we get its index 

        and find the number what when added will give as target
        if that number is in the hashmap, we return the index of that 
        number and the current index we are on

        if its not in the hashmap we will add that val in the the hashmap 

        overal time 
        """
        hash = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in hash:
                return [hash[comp], index]

            hash[num] = index
        return None