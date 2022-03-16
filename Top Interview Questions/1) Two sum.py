class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hash_table:              
                hash_table[nums[i]] = i
            else:
                return [hash_table[complement], i]

    
### Interview practice

'''
Brute force way : inefficient & has a runtime of n squared
We can do a lot better than brute force using a concept called complement.
Complement : the number derived by subtracting a number from a base number. For example, the tens complement of 8 is 2.
'''

'''
Hash table solution : has an O(n) runtime as well as time complexity
We would create a hash table with the key being current elements and the value being the index of that elements
and we're storing the index because that's what the question is asking to return.
'''


### Hash table
# f(key) -> hash code -> index -> value
# 
