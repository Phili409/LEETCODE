# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

 
# Example 1:
case1 = ([1,3], [2])
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
case2 = ([1,2], [3,4])
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

def merge(left, right):
    left_index, right_index = 0,0
    merged_list = []
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        elif left[left_index] > right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1
        else:
            merged_list.append(left[left_index])
            merged_list.append(right[right_index])
            left_index += 1
            right_index += 1
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list

def merge_sort(arr):
    if len(arr) <= 1: return arr
    
    Middle = len(arr) // 2
    left_list = arr[:Middle]
    right_list = arr[Middle:]
    
    left_sort = merge_sort(left_list)
    right_sort = merge_sort(right_list)
    return merge(left_sort, right_sort)


def find_median(arr1:list, arr2:list):
    arr1.extend(arr2)
    sorted_array = merge_sort(arr1)
    is_even = True if (len(sorted_array) % 2)==0 else False
    
    return (sorted_array[len(sorted_array) // 2 -1] + sorted_array[(len(sorted_array) // 2) ]) / 2 if is_even else sorted_array[len(sorted_array) // 2] 

#print(find_median(case1[0], case1[1]))
#print(find_median(case2[0], case2[1]))



# ! Other way 

def median_sorted_array(arr1, arr2):
    left_pointer, right_pointer = 0,0
    sorted_list = []
    
    while (left_pointer < len(arr1)) and (right_pointer < len(arr2)):
        if arr1[left_pointer] < arr2[right_pointer]:
            sorted_list.append(arr1[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(arr2[right_pointer])
            right_pointer += 1
    sorted_list.extend(arr1[left_pointer:])
    sorted_list.extend(arr2[right_pointer:])
    is_odd = True if (len(sorted_list) % 2 == 0) else False
    middle_index = len(sorted_list) // 2 
    return (sorted_list[middle_index] + sorted_list[middle_index-1]) / 2  if is_odd else float(sorted_list[len(sorted_list)//2])


print(median_sorted_array(case1[0], case1[1]))
print(median_sorted_array(case2[0],case2[1]))
    
            
            
        
    

            