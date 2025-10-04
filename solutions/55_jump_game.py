"""
LeetCode Problem: 55. Jump Game
Difficulty: Medium
URL: https://leetcode.com/problems/jump-game/

Problem Description:
You are given an integer array nums. You are initially positioned at the array's 
first index, and each element in the array represents your maximum jump length 
at that position.

Return true if you can reach the last index, or false otherwise.

Examples:
- Input: nums = [2,3,1,1,4] -> Output: true
- Input: nums = [3,2,1,0,4] -> Output: false

Approach: [Your approach here]

Time Complexity: O(?)
Space Complexity: O(?)
"""

from typing import List

def canJump(nums: List[int]) -> bool:
    far = 0
    for i, jumps in enumerate(nums):
        if i > far:
            return False
        far = max(far, i + jumps)
        if far >= len(nums) - 1:
            return True
    return True


# Test cases
if __name__ == "__main__":
    # Test case 1: [2,3,1,1,4] → true
    nums1 = [2, 3, 1, 1, 4]
    result1 = canJump(nums1)
    print(f"Test 1: nums = {nums1}, result = {result1}")
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: [3,2,1,0,4] → false
    nums2 = [3, 2, 1, 0, 4]
    result2 = canJump(nums2)
    print(f"Test 2: nums = {nums2}, result = {result2}")
    assert result2 == False, f"Expected False, got {result2}"
    
    # Test case 3: [0] → true (single element)
    nums3 = [0]
    result3 = canJump(nums3)
    print(f"Test 3: nums = {nums3}, result = {result3}")
    assert result3 == True, f"Expected True, got {result3}"
    
    # Test case 4: [1,0] → true (can jump over 0)
    nums4 = [1, 0]
    result4 = canJump(nums4)
    print(f"Test 4: nums = {nums4}, result = {result4}")
    assert result4 == True, f"Expected True, got {result4}"
    
    # Test case 5: [0,1] → false (stuck at first position)
    nums5 = [0, 1]
    result5 = canJump(nums5)
    print(f"Test 5: nums = {nums5}, result = {result5}")
    assert result5 == False, f"Expected False, got {result5}"
    
    # Test case 6: [2,0,0] → true
    nums6 = [2, 0, 0]
    result6 = canJump(nums6)
    print(f"Test 6: nums = {nums6}, result = {result6}")
    assert result6 == True, f"Expected True, got {result6}"
    
    # Test case 7: [1,2,3] → true
    nums7 = [1, 2, 3]
    result7 = canJump(nums7)
    print(f"Test 7: nums = {nums7}, result = {result7}")
    assert result7 == True, f"Expected True, got {result7}"
    
    # Test case 8: [1,1,1,0] → true
    nums8 = [1, 1, 1, 0]
    result8 = canJump(nums8)
    print(f"Test 8: nums = {nums8}, result = {result8}")
    assert result8 == True, f"Expected True, got {result8}"
    
    print("✅ All test cases passed!")
