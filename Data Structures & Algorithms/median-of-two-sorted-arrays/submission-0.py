class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        merges the two arrays asnd find their middle values using binary 
        search


        Conditions:
        Since both arrays are sorted it will be easier to. merge them 
        or is there a way to do this differntly and on each array find the 
        middle in the first array find the middle in the second array and  return 

        Now if they are even number of elements in both elements:
            return the the average of the middle two

        if odd number return the the middle number of merging 

        """
    
        A, B = nums1, nums2 
        if len(A) > len(B):
            A, B = B, A 

        m, n = len(A), len(B)

        left = 0 
        right = m 

        total = m + n 

        half = total // 2 

        while left <= right: 
            i =  (left + right) //2 
            j = half - i 

            A_left = A[i -1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")

            B_left = B[j -1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return  float(min(A_right, B_right))

                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                right = i -1 

            else:
                left = i + 1 






