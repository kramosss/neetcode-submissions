class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, m in enumerate(nums):
            diff = target - m
            if diff in a:
                return [a[diff], i]
            a[m] = i
        return

        