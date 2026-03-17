nums1 = input().split()
nums2 = input().split()
nums3 = input().split()

set_one_two = set(nums1).intersection(nums2)
set_three = set_one_two.difference(nums3)

result_list = [int(el) for el in set_three]
print(*sorted(result_list, reverse=True))
