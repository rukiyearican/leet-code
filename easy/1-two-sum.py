class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {} # val: index
                          # every element that comes before the current home that
                          # every previous element is going to stored in this map
        for i, n in enumerate(nums):
            diff = target - n
            if diff in previous_map:
                return [previous_map[diff], i]
            previous_map[n] = i 