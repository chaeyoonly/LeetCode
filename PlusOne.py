class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in reversed(range(length)):
            while digits[i] == 9:
                digits[i] = 0
                if(i-1 < 0):
                    digits.insert(0,1)
                break
            else:
                digits[i] += 1
                break
       
        return digits
