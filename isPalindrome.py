class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palin = ''.join(i.lower() for i in s if i.isalnum())
        left, right = 0, len(palin) - 1
        while left < right:
            if palin[left] != palin[right]:
                return False
            left += 1
            right -= 1
        return True