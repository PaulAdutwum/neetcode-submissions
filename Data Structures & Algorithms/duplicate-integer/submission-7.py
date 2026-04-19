class Solution:
    def hasDuplicate(self, nums):
        """
        Input:
            - nums -> list of intergers given

        Output:
            - Boolean - True if duplicates False otherwise

        Goal:
            - Return True or False 

        Notes:
            ** Will nums ever be empty?
            ** What should i return if nums is empty?
            ** Will nums contain only integers?
            ** Will nums have negative nums?
            ** Any edge case i am missing right now?

        Approach:
        1. Initialize a set called seen
        2. Loop over array
        3. check if nums[i] in set
            if nums[i] in set:
                return True 
            return False otherwise 

        
        """
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
            

        
    
         