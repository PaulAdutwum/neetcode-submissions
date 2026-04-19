class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input:
            - nums - array of ints
            - target 

        Output:
            - integer representing the index of target in the array
        Goals
         - return the index of target 

        Notes:
            - Will the array always be sorted?
            - Will the array nums always contain positive ints?
            - Will the array ever be empty?
            - What should i return if the array is empty?
            - What is the elements in the array are repeating?
            -What should i return in the target cannot be found?

        Approach:
            - left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right)// 2
                if nums[mid] = target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1 

            return mid 




        """

        left, right = 0, len(nums) -1 
        mid = -1 
        while left <= right:
            mid = (right + left)// 2

            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                left = mid + 1
            else:
                right = mid -1 
        left += 1
        right -= 1 


        return -1
        