nums = [-2,1,-3,7,-2,2,1,-5,4]
dp = [0 for i in nums]
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print( max(dp))