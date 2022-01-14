# Time Limit Exceeded 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        breaker = False
        for i in range(0, length):
            for j in range(length-1, i, -1):
                if numbers[i] + numbers[j] == target:
                    breaker = True
                    break
            if breaker == True:
                break
        return [i+1,j+1]
      
  
### Two pointers Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1     
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
