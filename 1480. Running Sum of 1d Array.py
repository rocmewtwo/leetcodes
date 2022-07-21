from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            nums[i]+=sum
            sum+=num

        return nums

if __name__ == "__main__":
    input = [1,2,3,4]
    input = [3,1,2,10,1]
    result = Solution().runningSum(input)
    print(result)