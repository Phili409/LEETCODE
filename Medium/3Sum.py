# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
case1 = [-1,0,1,2,-1,-4]
case2 = [0,1,1]
case3 = [0,0,0]

def threesome(nums:list):
    ans = []
    nums.sort()
    for left in range(len(nums) - 2):
        if left > 0 and nums[left] == nums [left + 1]:continue
        middle = left + 1
        right = len(nums)-1
        
        while middle < right:
            sum_of_numbers = nums[left]+nums[middle]+nums[right]
            if sum_of_numbers > 0: right -= 1
            if sum_of_numbers < 0: middle += 1
            else:
                ans.append([nums[left],nums[middle],nums[right]])
                while middle < right and nums[middle] == nums[middle+1]: middle += 1
                while middle < right and nums[right] == nums[right-1]:right -= 1
            middle += 1
            right -= 1
    return ans    

#print(threesome(case1))
#print(threesome(case2))
#print(threesome(case3))

        
def tresome(nums:list):
    answer = []
    nums.sort()
    
    for left_index in range(len(nums)-2):
        if left_index > 0 and nums[left_index] == nums[left_index + 1]:continue
        
        middle_index = left_index + 1
        right_index = len(nums) - 1
        
        while middle_index < right_index:
            sum_of_index = nums[left_index]+nums[middle_index]+nums[right_index]
            if sum_of_index > 0: right_index -= 1
            if sum_of_index < 0: middle_index += 1
            else:
                answer.append([nums[left_index],nums[middle_index],nums[right_index]])
                while middle_index < right_index and nums[middle_index] == nums[middle_index + 1]: middle_index += 1
                while middle_index < right_index and nums[right_index] == nums[right_index - 1]: right_index -= 1
            middle_index += 1
            right_index -= 1
    return answer
print(tresome(case1))
print(tresome(case2))
print(tresome(case3))


