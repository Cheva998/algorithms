from collections import Counter
from typing import List

class Solution:
    """
    This solution was made with some research, the third and final attempt
    parses the array backwards
    """
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = set()
        operations = 0
        # Parse until -2 to include the case where all elements are unique
        for i in range(n-1, -2, -1):
            num = nums[i]
            if num in freq:
                break
            freq.add(num)
        operations = (i + 3) // 3
        return operations
        

class Solution1:
    """
    This solution was the first attempt, it gives correct results but also a 
    "time limit exceeded" on leetcode
    """
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        remove_items = 3
        while len(nums) >= remove_items:
            has_repeated = self.hasRepeated(nums)
            if has_repeated:
                nums = nums[remove_items:]
                operations += 1
            else:
                return operations
            
        has_repeated = self.hasRepeated(nums)
        if operations > 0 and has_repeated:
            return operations + 1
        elif operations > 0 and not has_repeated:
            return operations

        if has_repeated:
            return operations + 1
        return operations

    def hasRepeated(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False


class Solution2:
    """
    This solution was my second attempt, it works, but it parses the whole
    array, making it a naive solution
    """
    
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        duplicates = sum(1 for v in freq.values() if v > 1)
        ops = 0
        if duplicates == 0:
            return ops
        
        n = len(nums)
        idx = 0
        while idx < n:
            for _ in range(3):
                if idx >= n:
                    break
                
                value = nums[idx]
                if freq[value] == 2:
                    duplicates -= 1
                freq[value] -= 1
                idx += 1
            ops += 1
            if duplicates == 0:
                return ops

        return ops


nums = [100,4,13,12,92,25,23,63,38,82,15,19,74,85,56,13,13]
nums = [1,2,1,3,2]
nums = [87,15,26,32,32,18]
#sol = Solution()
#sol.minOperations(nums)