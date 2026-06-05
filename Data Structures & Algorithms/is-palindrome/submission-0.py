class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            # Skip non-alphanumeric characters from the left
            while L < R and not self.alphaNum(s[L]):
                L += 1
            
            # Skip non-alphanumeric characters from the right
            while L < R and not self.alphaNum(s[R]):
                R -= 1
            
            # Compare the lowercase versions of the characters
            if s[L].lower() != s[R].lower():
                return False
            
            # Move both pointers inward
            L += 1
            R -= 1
            
        return True

    # Helper function MUST be indented exactly to the same level as def isPalindrome
    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))