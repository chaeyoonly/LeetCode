class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse = []
        i = 0
        j = len(s) - 1
        while i <= j:
            reverse.append(s[j])
            j -= 1
        s[:] = reverse
        
        
### Two Pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


### Simple ways to reverse the array
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1] # OR JUST s.reverse()
