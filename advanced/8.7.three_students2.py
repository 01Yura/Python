nums1 = input().split()
nums2 = input().split()
nums3 = input().split()

set1_2_3 = set(nums1).intersection(nums2).intersection(nums3)
common_list = nums1 + nums2 + nums3
common_list.sort()
new_set = set()
for el in common_list:
    if el not in set1_2_3:
        new_set.add(int(el))

print(*sorted(new_set))
