# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule 
# and false otherwise.

#Example 1:
case1 = ([1,0,0,0,1], 1)
#Input: flowerbed = [1,0,0,0,1], n = 1
#Output: true

#Example 2:
case2 = ([1,0,0,0,1], 2)
#Input: flowerbed = [1,0,0,0,1], n = 2
#Output: false

# Example 3:
case3 = ([0,0,1,0,1], 1)

def can_plant(case:tuple):
    flowerbed, number_to_plant = case
    pointer = 0
    next_pointer = 2
    
    while number_to_plant > 0 and pointer < len(flowerbed):
        if flowerbed[pointer] == 1: pointer += next_pointer
        else:
            if flowerbed[pointer+1] == 0 and (pointer==0 or flowerbed[pointer-1]!=1):
                flowerbed[pointer] = 1
                number_to_plant -= 1
                pointer += next_pointer
            else: pointer += 1
    print(flowerbed)
    return number_to_plant == 0

print(can_plant(case1))
print(can_plant(case2))
print(can_plant(case3))


            
        
            
 