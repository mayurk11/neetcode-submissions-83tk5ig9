class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for ch in s.lower():
            if ch.isalnum():
                filtered += ch
        
        rev = ""
        for ch in filtered:
            rev = ch + rev

        if rev == filtered:
            return True
        return False
