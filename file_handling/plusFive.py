nums = [10, 20, 30]
nums[0] = 80
print(nums) # [20, 20, 30]

for i in range(len(nums)):
    nums[i] = nums[i] + 10

print(nums)