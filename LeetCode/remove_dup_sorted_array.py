class Solution:
    """
    Pseudo-code:
    Early exit: length <= 2 return length
    1. Initialize indexes k=1 (for twice unique) i=2 (for parsing)
    2. Compare elements k-1 to i
    3. If elements is different, the k+1, and update element k = element i
    4. If there are more elements go to 2, else return k + 1
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        "Each element appear at most twice"
        n = len(nums)
        if n <= 2:
            return n
        k=1
        for i in range(2, n):
            if nums[k-1] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1