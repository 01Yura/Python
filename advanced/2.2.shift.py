nums = input().split()
nums.insert(0, nums[-1])
nums = nums[:-1]
print(*nums)
