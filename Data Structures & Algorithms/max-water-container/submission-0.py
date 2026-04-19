class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        This is classic two pointe problem

        Input:
            ** Heights - array of ints

        Output: 
            ** lenghts with max container area

        Goal:
            * return the heihgt pair that gives the maximum area 


        Appraoch:
            0. initialize left, right and max_container, current_container  

            1. start with left pointer at index 0
            2. cerate right pointer at index n - 1

            3. find the aea of container produced given those areas
                area = length * width = min(h[l], h[r]) * [right - left]
                max_container = max(max_container, area)


            if h[lleft] height is less than h[iright]:
                left += 1

            if height at the h[right] <= height[left]:
                right -= 1 

            max_container = max


            
        """
        left, right = 0, len(heights) - 1

        max_water = 0 

        while left < right:
            area = (right - left)* min(heights[left], heights[right])
            max_water = max(max_water, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -= 1

        return max_water 
        