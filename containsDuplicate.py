class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        comp = set(nums)
        return len(comp) != len(nums)
        