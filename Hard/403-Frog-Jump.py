 # ! 403 Frog Jump

# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. 
# The frog can jump on a stone, but it must not jump into the water.

# Given a list of stones positions (in units) in sorted ascending order, 
# determine if the frog can cross the river by landing on the last stone. 
# Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
# The frog can only jump in the forward direction.

# Example 1:
case1 = [0,1,3,5,6,8,12,17]
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, 
# then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 
# 4 units to the 7th stone, and 5 units to the 8th stone.

# Example 2:
case2 = [0,1,2,3,4,8,9,11]
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


def frog_jump(stones:list):
    # dictionary [stone_map] -> used as a graph having a set [vertices or connections] 
    # -> being the previous jump distances needed to satisfy a jump
    stone_map = {stone : set() for stone in stones}
    # Innitial base case where k [jumping distance] is initialized by 1 so we add initial stone [0] from stones[0] and add the vertex [0]
    # This ensures the first jump is always 1
    stone_map[0].add(0)
    
    # Iterate through every stone in the list [stones]
    for stone in stones:
        # Iteratate through every connection/vertex within the set -> 
        # stone_map[stone] -> will contain the connections being the VALID jumping distances to get to said stone position
        for jumps in stone_map[stone]:
            # Since every jumping distance can be either, k [k=current_jump_distance] or k-1 or k+1
            # We iterate through each possible jumping distance to determine if the frog can reach a new stone
            for jump_distance in [jumps-1, jumps, jumps+1]:
                # Check if the jumping distance is > 0 since the frog cannot go backwards and must be atleast 1 to initiate
                # Also checks if the sum of the (current_stone + jump_distance[0 or, 1 or, 2]) is equal to a stone in [stone_map]
                if jump_distance > 0 and ((stone + jump_distance) in stone_map):
                    # If both conditions are satisfied then the distance requiered to jump from stone x to the new stone in the map 
                    # is added to the set of possible jump_distances requiered to get from a previous stone x to the new stone_map[stone]
                    stone_map[jump_distance+stone].add(jump_distance)
            # After checking through all 3 possible jumping distances the for loop is complete and then moves to ->
            # jumps + 1 -> in stone_map[stone] if any, else ->
        # If there is no more vertecies/connections for that stone, then ->
    # The code will iterate to the next stone in the list and continue iterrating through until the last stone
    
    # ! len(stone_map[stones[-1]]) counts the amount of elements in the last stone's set
    # ! Meaning that in order for the frog to make it to the last stone -> stones[-1] there must be atleast one possible jump in the set
    return len(stone_map[stones[-1]]) > 0

print(frog_jump(case1))
print(frog_jump(case2))

        
    
    