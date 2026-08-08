class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize left (l) and right (r) pointers
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric characters from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
                
            # Compare lowercase character values
            if s[l].lower() != s[r].lower():
                return False
                
            # Move both pointers inward
            l, r = l + 1, r - 1
            
        return True

    def alphaNum(self, c: str) -> bool:
        # Custom manual implementation of s.isalnum()
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
