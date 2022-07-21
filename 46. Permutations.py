## 46. Permutations

from readline import insert_text
from typing import Dict, List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dps = [[nums[0]]]

        # current num
        for num in nums[1:]:
            res = []
            for dp in dps:
                res += self.insert(num, dp)

            dps = res

        return dps

    def insert(self, num: int, nums: List[int]) -> List[List[int]]:
        r = []
        for i in range(len(nums)+1):
            r.append(nums[:i] + [num] + nums[i:])
        return r

if __name__ == "__main__":
    input = [1, 2, 3, 4]
    result = Solution().permute(input)
    print(result)

    # print(Solution().insert(5, input))

