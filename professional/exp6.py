import sys

nums = [1, 2, 3]                            # ссылка 1
nums1 = nums                                # ссылка 2
nums2 = nums1                               # ссылка 3
temp = [4, 5, 6, nums, nums1, nums2]        # ссылка 4, 5, 6
print(sys.getrefcount(nums))                # ссылка 7