from collections import Counter
import heapq
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

        Heaps approach:
        Find frequency using a hashmap
        Use heaps to store values key pairs 
        pop form heap to get log n solutions

        Bucket sort apprach:
        optimal solution for this problem
        learn aboout bucket sort and use to solve this proble for me


        """
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        # freq_arr = []
        # for num, count in seen.items():
        #     freq_arr.append([count, num])

        # freq_arr.sort()

        heap = []
        for num in seen.keys():
            heapq.heappush(heap, (-seen[num], num))

        res = []
        while len(res) < k:
            val = heapq.heappop(heap)
            res.append(val[1])

        return res


        


    
           
       


        

        