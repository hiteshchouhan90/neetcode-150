class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_list :list = []
        for num in nums:
            if num in value_list:
                return True
            else:
                value_list.append(num)
        return False