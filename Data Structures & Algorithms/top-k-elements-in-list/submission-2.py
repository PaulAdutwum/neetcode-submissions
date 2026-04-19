from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        Input:
        Nums - array list 
        k - integer

        Output:
        list of k frequent elements in nums

        Goal:
        return the list of top frequent elements in k

        Notes:
            ** Will nums be empty?
            ** What should i return is nums is empty?
            ** Will nums con tain negative vals?
            ** Will nums aonly contain int values
            ** What is expected time cmplexity for this solution?
            ** Should i assume that nums will always be sorted?
            ** 

        Approach:
        Use hashmap to get frequency of numbers in nums
        Use list to. store value sin and their frequenciis
        Sort the list if nums is not already sorted for
        Use another list to store results
        loop over the and pop elements int to the resutls list


        """
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        freq_arr = []
        for num, count in seen.items():
            freq_arr.append([count, num])

        freq_arr.sort()

        res = []
        while len(res) < k:
            res.append(freq_arr.pop()[1])

        return res


        


    
           
       


        

        