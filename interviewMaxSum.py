# 使用动态规划 达成时间复杂度O(n) 为此要创建一个数组 起名dp
# 思路是把所有以index i结尾的子数组们考虑到 计算出来这些子数组中元素之和最大的是多少 存到dp中 存起来的目的是方便之后使用 避免重复运算（即动态规划的本质）
# 例如 list= [-2,1,-3,7,-2,2,1,-5,4] 则 
#   在index=0 时 所有可能的子数组只有一个 就是它自己 即-2 所以此时我们存一个       [-2,0, 0, 0...]
#   在index=2 时 可能的子数组 有 [-2, 1]和[1], 对比可得 -2+1与1 最大值为1， 所以存[-2,1, 0, 0...]
#   在index=3 时 解释一下动态规划的妙用， 此时我们已经保存了 以index=2结尾的所有子数组 最大sum（sublist)是 1（数值储存在dp[2])，
#                所以此时 来了一个新数-3，只有两种情况 1 我们要一个子数组它  包含list[3]和 前面的数（注意前面连续数的和 它的最大值我们已经计算过了并存在了dp[2]中）
#                                                   2 我们要一个子数组它只包含list[3] 
#                即只比较 1+（-3)和 -3， 最  大  值  为-2   所  以  此  时  存   [-2,1,-2,0...]
# 最终dp = [-2, 1, -2, 7, 5, 7, 8, 3, 7] 即当以index=6 作为子数组末端时 存在子数组 其元素之和是最大值8
nums = [-2,1,-3,7,-2,2,1,-5,4]
dp = [0 for i in nums]
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print( max(dp))
