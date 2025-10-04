# LeetCode Problem Analysis Template

## Problem Details
- **Problem Number**: 55
- **Problem Name**: Jump Game
- **Difficulty**: Medium
- **URL**: https://leetcode.com/problems/jump-game/
- **Date Solved**: [To be filled]

## Problem Description
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Examples
```
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Initial Thoughts
- This is a greedy problem where we need to determine if we can reach the end
- Key insight: We don't need to track the exact path, just if it's possible
- We can track the "furthest reachable position" as we iterate
- If at any point we can't move forward from the current position, return false

## Solution Approaches

### Approach 1: Greedy - Track Maximum Reachable Position
**Pattern Used**: Greedy Algorithm

**Algorithm**:
1. Initialize `max_reach = 0` (furthest position we can reach)
2. Iterate through the array
3. For each position `i`, check if `i <= max_reach` (can we reach this position?)
4. If yes, update `max_reach = max(max_reach, i + nums[i])`
5. If at any point `i > max_reach`, return false
6. Return true if we can reach the last index

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Pros**:
- Single pass through the array
- Optimal time complexity
- No extra space needed
- Intuitive greedy approach

**Cons**:
- Requires understanding of greedy principle

**Code**:
```python
def canJump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        
        # Early termination if we can already reach the end
        if max_reach >= len(nums) - 1:
            return True
    
    return True
```

### Approach 2: Dynamic Programming (Alternative)
**Pattern Used**: Dynamic Programming

**Algorithm**:
1. Create dp array where dp[i] represents if we can reach position i
2. Initialize dp[0] = True
3. For each position, check all previous positions that could reach it
4. Return dp[n-1]

**Time Complexity**: O(n²)
**Space Complexity**: O(n)

**Pros**:
- More intuitive for some people
- Clearly shows reachability for each position

**Cons**:
- Less efficient than greedy approach
- Uses extra space

## Chosen Solution
**Greedy approach** - more efficient and elegant for this problem type.

## Key Insights
- **Greedy principle**: We only need to track the furthest reachable position
- **Early termination**: Once we can reach the end, we can return true immediately
- **Failure condition**: If current position is beyond our reach, it's impossible
- **This pattern applies to**: Jump Game II, Gas Station, and other reachability problems

## Related Problems
- Jump Game II (minimum jumps)
- Gas Station (circular reachability)
- Can Place Flowers (similar greedy logic)

## Test Cases
```python
# Test case 1: Can reach end
assert canJump([2,3,1,1,4]) == True

# Test case 2: Cannot reach end
assert canJump([3,2,1,0,4]) == False

# Edge cases
assert canJump([0]) == True  # Single element
assert canJump([1,0]) == True  # Can jump over 0
assert canJump([0,1]) == False  # Stuck at first position
```

## Notes
- The key insight is that we don't need to simulate jumps, just track reachability
- This is a classic greedy problem where local optimal choices lead to global optimum
- The algorithm essentially asks: "Can I reach position i?" for each i
