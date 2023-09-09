nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

def product_except_self(nums:list):
    lenght = len(nums)
    ans = [1]*lenght
    left= 0
    
    for index in range(lenght):
        while left < lenght:
            if left != index: 
                ans[index] *= nums[left]
            left += 1
        left= 0
    return ans
def product_except_self(nums:list):
    lenght = len(nums)
    ans = [1]*lenght
    
    for index in range(lenght):
        map(lambda x: ans[index] * x, nums[::index])
        map(lambda x: ans[index] * x, nums[index::])
        
    return ans

print(product_except_self(nums1))
print(product_except_self(nums2))

    
    

    
     
    