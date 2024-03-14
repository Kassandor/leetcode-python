from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = dict()

        for index, num in enumerate(nums):
            difference = target - num
            if difference in nums_to_index:
                return [nums_to_index.get(difference), index]
            if not num in nums_to_index:
                nums_to_index.update({num: index})

        return []

print(Solution().twoSum([2, -5, 11, -5], -10))
