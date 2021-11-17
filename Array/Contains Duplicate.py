class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = 0
        i = 0
        j = 1
        length = len(nums) - 1
        nums.sort()
        while duplicate < 1 and length != 0:
            if(nums[i] == nums[j]):
                duplicate += 1
            elif(j == length):
                break
            else:
                i += 1
                j += 1

        return False if duplicate < 1 else True
