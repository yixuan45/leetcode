# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []  # 用于存放答案
        nums.sort()  # 先将数组排成有序序列，执行后nums就变成有序的数组
        for i in range(0, len(nums) - 2):  # 固定好一个点
            j = i + 1
            k = len(nums) - 1
            if (nums[i] + nums[k - 1] + nums[k]) < 0 or (nums[i] + nums[j] + nums[j + 1]) > 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ret


if __name__ == '__main__':
    ret = Solution()
    print(ret.threeSum([-1, 0, 1, 2, -1, -4]))
