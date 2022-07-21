## 213. House Robber II

from typing import List

class Solution:
    def robBasic(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        ## [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robBasic(nums[1:]), self.robBasic(nums[:-1]))

if __name__ == "__main__":
    nums = [0]
    # nums = [2,3,2]
    # nums = [1,2,3,1]
    # nums = [1,2,3]
    # nums = [1,2,1,1]
    # nums = [200,3,140,20,10]

    print(Solution().rob(nums))