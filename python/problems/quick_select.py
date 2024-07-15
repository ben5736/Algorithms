import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthLargestInternal(nums[:], k - 1, 0, len(nums) - 1)
    
    def findKthLargestInternal(self, nums, k, start, end):
        pivot = random.randint(start, end)
        pivot_after_shuffle = self.shuffle(nums, pivot, start, end)
        if pivot_after_shuffle == k:
            return nums[pivot_after_shuffle]
        elif pivot_after_shuffle > k:
            return self.findKthLargestInternal(nums, k, start, pivot_after_shuffle - 1)
        else:
            return self.findKthLargestInternal(nums, k, pivot_after_shuffle + 1, end)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def shuffle(self, nums, pivot, start, end):
        pivot_val = nums[pivot]
        self.swap(nums, pivot, end)

        cur_start = start
        cur_end = end - 1
        while cur_start <= cur_end:
            if nums[cur_start] >= pivot_val:
                cur_start += 1
            else:
                self.swap(nums, cur_start, cur_end)
                cur_end -= 1
        self.swap(nums, cur_start, end)
        return cur_start


import unittest

class Test(unittest.TestCase):

  def test1(self):
    self.assertEqual(Solution().findKthLargest([3,2,1,5,6,4], 2), 5)

  def test2(self):
    self.assertEqual(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)

if __name__ == '__main__':
    unittest.main()