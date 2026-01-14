from typing import List

class Solution:
    """
    Pseudo-code: (with a bit of research ;)
    1. Create a function that reverses the array
     a. Given two indexes left and right shift the values of the indexes
     b. Increase left and decrease right
     c. If left > right end, else go to a.
    2. Reverse the whole array
    3. Reverse the first part from 0 to k
    4. Reverse the second part from k to last

    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                old_l = nums[left]
                old_r = nums[right]
                nums[left] = old_r
                nums[right] = old_l
                left += 1
                right -= 1
        n = len(nums)
        k = k % n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

class Solution2:
    """
    Pseudo-code:
    1. Initialize a new array of size n
    2. Initialize the parsing with index i
    3. Save the i number in position (i+k) % N of new array
    4. When it's done we need to parse the new array to change
    the values of the old array (because it needs to be in-place)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        new_arr = [0] * n
        for i in range(n):
            idx = (i + k) % n
            new_arr[idx] = nums[i]
        for i in range(n):
            nums[i] = new_arr[i]

