class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = 0
        i = 0
        j = 1
        length = len(nums) - 1
        while duplicate < 1 and length != 0:
            if(nums[i] == nums[j]):
                duplicate += 1
            elif(i == length-1 and j == length):
                break
            elif(j == length):
                i += 1
                j = i + 1
            else:
                j += 1

        return False if duplicate < 1 else True
