class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = []
        for i in nums:
            array.append(pow(i,2))
        array.sort()
        return array
      
