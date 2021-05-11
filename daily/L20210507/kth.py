"""
寻找两个有序数组的第k个元素
"""
from typing import List

"""
寻找两个有序数组的第k个元素
递归写法
"""


def kth(nums1: List[int], nums2: List[int], k: int) -> int:
    # 处理边界条件
    if not nums1: return nums2[k]
    if not nums2: return nums1[k]

    mid_1 = len(nums1) // 2
    mid_2 = len(nums2) // 2
    v_1 = nums1[mid_1]
    v_2 = nums2[mid_2]

    if mid_1 + mid_2 < k:
        if v_1 > v_2:
            # mid_1 + mid_2 < k, 说明mid_1 + mid_2 最大为k-1，第k个元素也是排序后的第k-1个元素
            # 如果v_1 > v_2，极端情况下v_1占着下标k-1
            # 所以，
            # 可以确认k不可能出现在nums2[:mid_2+1]范围内
            return kth(nums1, nums2[mid_2+1:], k - mid_2 - 1)
        else:
            # 可以确认k不可能出现在nums1[:mid_1+1]范围内
            return kth(nums1[mid_1+1:], nums2, k - mid_1 - 1)
    else:
        # mid_1 + mid_2 >= k ，极端情况下，mid_1 + mid_2 占着下标k
        # 第k个元素在下标k的左侧
        if v_1 > v_2:
            # 在上述极端情况下，v_1 占着下标k，所以k不可能出现在nums1[mid_1:]范围内
            return kth(nums1[:mid_1], nums2, k)
        else:
            # 同理，在极端情况下，v_2占着下标k，所以k不可能出现在nums2[mid_2:]范围内
            return kth(nums1, nums2[:mid_2], k)

"""
迭代写法
"""


import unittest


class TestKth(unittest.TestCase):
    def test_kth(self):
        self.assertEqual(kth([3, 6, 8, 9], [2, 4, 5, 8], 4), 6)