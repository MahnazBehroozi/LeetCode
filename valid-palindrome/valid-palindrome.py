class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(l for l in s.lower() if l.isalnum())
        if(s == s[::-1]):
            return True
        return False
