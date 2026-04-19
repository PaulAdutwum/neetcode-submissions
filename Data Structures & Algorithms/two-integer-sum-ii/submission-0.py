class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        if not numbers:
            return[]

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left +1, right + 1]

            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [numbers[left], numbers[right]]

        


        
            
        

        return []
        