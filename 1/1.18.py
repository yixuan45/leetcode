# -*- coding: utf-8 -*-
"""给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # 数据先变成顺序
        ret = []
        """定义变量"""
        i = 0  # 第一个指针
        j = 0  # 第二个指针
        k = 0  # 第三个指针
        l = 0  # 第四个指针
        for i in range(0, len(nums) - 3):
            x = nums[i]
            if i and x == nums[i - 1]:  # 跳过重复数字
                continue
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                # 优化三，如果nums[j]和nums[j-1]相同，则跳过此次循环
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:
                    continue
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = x + y + nums[k] + nums[l]
                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        ret.append([x, y, nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return ret


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    sol = Solution()
    print(sol.fourSum(nums, target=0))
