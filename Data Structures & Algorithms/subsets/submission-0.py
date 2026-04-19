class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start_index, curr_path):
            res.append(list(curr_path))

            for i in range(start_index, len(nums)):
                curr_path.append(nums[i])

                backtrack(i +1, curr_path)

                curr_path.pop()

        backtrack(0, [])

        return res

        