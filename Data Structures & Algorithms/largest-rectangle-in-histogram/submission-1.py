class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Here is what I am considering for an answer:

        Input:
            array of ints - heights
                heights[i] is the height of. particular bar


        Output:
             the area of the longest rectangle 
            can be formed from all the bats

        Goal:
        Return the area of the longest recatangle can be formed
        from all the bars in the heights


        Approach:

            First what is area?
                Area is lenght x width

                - We know all the heights already heights[i]
                - with for each bar is one

            for the first bar, 
            area = heights[i] x 1 

            for the second bar: 
                area is heights[i] x (1 +1)

            for the third bar,
            area = heights[i] x (1 +1 +1)



        We know the width cannot tbe larger than the 
        length of the array itself 
        because if there are n bars in heights, the biggest
        width will be n 



        - we can create variable called 
        area = 0 

        width = 1 

        n = len(heights)

        for i in range(n):
            curr_area = heights[i] x width
            

            
            area = max(curr_area, area)
            width += 1 

        return area

        

        """

        max_area = 0 
        stack = []


        for i, h in enumerate(heights): 
            start = i 

            while stack and stack[-1][-1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height *(i -index))
                start = index

            stack.append((start, h))
        n = len(heights)
        for index, height in stack:
            max_area = max(max_area, height * (n-index))

        return max_area







        