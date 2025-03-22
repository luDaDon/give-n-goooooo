import re

class Solution(object):
    def isPalindrome(self, s):
        new_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left = 0
        right = len(new_s) - 1

        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        