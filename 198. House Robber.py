
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        rob = [0] * l

        if l == 1:
            return nums[0]

        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for i in range(2, l):
            rob[i] = max(rob[i-1], rob[i-2] + nums[i])

        return rob[-1]

    def rob2(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        ## [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


if __name__ == "__main__":
    input = [2,7,9,3,1]
    # rob1 = Solution().rob(input)
    rob2 = Solution().rob2(input)
    print(rob2)