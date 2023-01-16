
nums = list(i for i in range(1, 1000001))

for i in range(len(nums)):
    for j in str(nums[i]):
        if str(nums[i]).count(j) > 1:
            nums.remove(nums[i])

print(nums)