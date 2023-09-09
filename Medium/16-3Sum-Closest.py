 # ! 3Sum Closest
 # ! Medium

 # ? Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
 # ? Return the sum of the three integers.
 # ? You may assume that each input would have exactly one solution.

# Example 1:
case1 = ([-1,2,1,-4], 1)
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
case2 = ([0,0,0], 1)
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Example 3:
case3 = ([1,1,1,0], -100)

# ^ Input is tuple (list[int], int) the list being the integers and int being the target

def closest3Sum(case:tuple):
    nums, target = case
    # closest_sum is what we return as the answer, used as a placeholder
    closest_sum = None
    nums.sort()
    
    for left in range(len(nums)-2):
        middle = left + 1
        right = len(nums)-1
        
        holder = closest_sum
        while middle < right:
            sum_of_nums = nums[left]+nums[middle]+nums[right]
            if sum_of_nums == target: return sum_of_nums
            
            if holder == None or abs(target - sum_of_nums) < holder[0]: holder = (abs(sum_of_nums - target), sum_of_nums)

            if sum_of_nums < target: middle += 1
            elif sum_of_nums > target: right -= 1
        closest_sum = holder
    return closest_sum[1]

print(closest3Sum(case1))
print(closest3Sum(case2))
print(closest3Sum(case3))