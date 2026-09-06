import math
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:   
        merged_list = []

        nums1_index = 0
        nums1_length = len(nums1)
        nums1_skip = False

        nums2_index = 0
        nums2_length = len(nums2)
        nums2_skip = False

        running = True
        while running:
            if nums1_length == 0:
                merged_list = nums2
                running = False
            if nums2_length == 0:
                merged_list = nums1
                running = False
            if len(merged_list) == (nums1_length + nums2_length):
                running = False
                continue
            if not(nums2_skip) and nums1[nums1_index] > nums2[nums2_index]:
                merged_list.append(nums2[nums2_index])
                if nums2_index + 1 < nums2_length:
                    nums2_index += 1
                else:
                     nums2_skip = True
                     nums2[nums2_index] = math.inf
            elif not(nums1_skip) and nums1[nums1_index] < nums2[nums2_index]:
                merged_list.append(nums1[nums1_index])
                if nums1_index + 1 < nums1_length:
                    nums1_index += 1
                else:
                     nums1_skip = True
                     nums1[nums1_index] = math.inf
            else: 
                merged_list.append(nums1[nums1_index])
                if nums1_index + 1 < nums1_length:
                    nums1_index += 1
                else:
                    nums1_skip = True
                    nums1[nums1_index] = math.inf

            # print(merged_list)

        # print(merged_list)
        center_floored = len(merged_list) // 2
        if len(merged_list) % 2 == 0:

            print(float(merged_list[center_floored-1] + merged_list[center_floored]) / 2.0)
            return(float(merged_list[center_floored-1] + merged_list[center_floored]) / 2.0)
        else:
            print(float(merged_list[center_floored]))
            return(float(merged_list[center_floored]))


findMedianSortedArrays([1, 2, 2, 4, 4], [2, 3, 3, 7])


# Description:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6