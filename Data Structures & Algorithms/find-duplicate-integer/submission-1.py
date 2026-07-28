class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        # return None


        slow = nums[0]
        fast = nums[0]


        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]


        return slow
        