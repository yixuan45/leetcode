# -*- coding: utf-8 -*-
"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
示例 2：
输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List


class Solution:
    def abs1(self, x, y):
        if x > y:
            return x - y
        else:
            return y - x

    def nums_count(self, nums, i, j, k):
        """用于计算三个值之和"""
        return nums[i] + nums[j] + nums[k]

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # 变成顺序
        ret = self.nums_count(nums, 0, 1, -1)  # 全局
        ret_old = 0  # 存储上一步的值
        ret_new = 0  # 初始化要输出的结果
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            ret_old = self.nums_count(nums, i, j, k)
            while k > j:
                ret_new = self.nums_count(nums, i, j, k)
                if ret_new > target:
                    k -= 1
                    if self.abs1(ret_new, target) > self.abs1(ret_old, target):
                        """说明这一次结果比上一次结果更大"""
                        break
                    else:
                        """说明这一次结果比上一次结果更小"""
                        ret_old = ret_new
                else:
                    j += 1
                    if self.abs1(ret_new, target) > self.abs1(ret_old, target):
                        break
                    else:
                        ret_old = ret_new
            if self.abs1(ret, target) > self.abs1(ret_old, target):
                ret = ret_old
        return ret


if __name__ == '__main__':
    nums = [13, 252, -87, -431, -148, 387, -290, 572, -311, -721, 222, 673, 538, 919, 483, -128, -518, 7, -36, -840,
            233, -184, -541, 522, -162, 127, -935, -397, 761, 903, -217, 543, 906, -503, -826, -342, 599, -726, 960,
            -235, 436, -91, -511, -793, -658, -143, -524, -609, -728, -734, 273, -19, -10, 630, -294, -453, 149, -581,
            -405, 984, 154, -968, 623, -631, 384, -825, 308, 779, -7, 617, 221, 394, 151, -282, 472, 332, -5, -509, 611,
            -116, 113, 672, -497, -182, 307, -592, 925, 766, -62, 237, -8, 789, 318, -314, -792, -632, -781, 375, 939,
            -304, -149, 544, -742, 663, 484, 802, 616, 501, -269, -458, -763, -950, -390, -816, 683, -219, 381, 478,
            -129, 602, -931, 128, 502, 508, -565, -243, -695, -943, -987, -692, 346, -13, -225, -740, -441, -112, 658,
            855, -531, 542, 839, 795, -664, 404, -844, -164, -709, 167, 953, -941, -848, 211, -75, 792, -208, 569, -647,
            -714, -76, -603, -852, -665, -897, -627, 123, -177, -35, -519, -241, -711, -74, 420, -2, -101, 715, 708,
            256, -307, 466, -602, -636, 990, 857, 70, 590, -4, 610, -151, 196, -981, 385, -689, -617, 827, 360, -959,
            -289, 620, 933, -522, 597, -667, -882, 524, 181, -854, 275, -600, 453, -942, 134]
    target = -2805
    app = Solution()
    print(app.threeSumClosest(nums=nums, target=target))
