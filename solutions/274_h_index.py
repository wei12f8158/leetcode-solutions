"""
LeetCode Problem: 274. H-Index
Difficulty: Medium
URL: https://leetcode.com/problems/h-index/

Problem Description:
Given an array of integers citations where citations[i] is the number of citations 
a researcher received for their i-th paper, return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.

Examples:
- Input: citations = [3,0,6,1,5] → Output: 3
- Input: citations = [1,3,1] → Output: 1

Approach: Greedy Algorithm with Sorting
1. Sort citations in descending order
2. Iterate through sorted citations
3. For each position i (1-indexed), check if citation >= i
4. The h-index is the maximum i where citation >= i

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) if sorting in-place, O(n) if creating new array
"""

from typing import List

def hIndex(citations: List[int]) -> int:
    """
    Calculate the h-index for a researcher given their citation counts.
    
    The h-index is the maximum value h such that the researcher has 
    published at least h papers with at least h citations each.
    
    Args:
        citations: List of integers representing citation counts for each paper
        
    Returns:
        Integer representing the h-index
    """
    h = 0
    citations.sort(reverse=True)  # Sort in descending order
    
    for i, citation in enumerate(citations, 1):  # 1-indexed positions
        if citation >= i:
            h = i
        else:
            break  # No need to continue, citations are sorted
    
    return h

# Alternative approach using binary search (for practice)
def hIndexBinarySearch(citations: List[int]) -> int:
    """
    Alternative approach using binary search for h-index calculation.
    This approach is more optimal for understanding the concept.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    citations.sort(reverse=True)
    left, right = 0, len(citations)
    
    while left < right:
        mid = (left + right + 1) // 2
        if mid <= len(citations) and citations[mid - 1] >= mid:
            left = mid
        else:
            right = mid - 1
    
    return left

# Test cases
if __name__ == "__main__":
    # Test case 1: [3,0,6,1,5] → 3
    citations1 = [3, 0, 6, 1, 5]
    result1 = hIndex(citations1)
    print(f"Test 1: citations = {citations1}, h-index = {result1}")
    assert result1 == 3, f"Expected 3, got {result1}"
    
    # Test case 2: [1,3,1] → 1
    citations2 = [1, 3, 1]
    result2 = hIndex(citations2)
    print(f"Test 2: citations = {citations2}, h-index = {result2}")
    assert result2 == 1, f"Expected 1, got {result2}"
    
    # Test case 3: [100] → 1
    citations3 = [100]
    result3 = hIndex(citations3)
    print(f"Test 3: citations = {citations3}, h-index = {result3}")
    assert result3 == 1, f"Expected 1, got {result3}"
    
    # Test case 4: [0,1,3,5,6] → 3 (sorted version of test case 1)
    citations4 = [0, 1, 3, 5, 6]
    result4 = hIndex(citations4)
    print(f"Test 4: citations = {citations4}, h-index = {result4}")
    assert result4 == 3, f"Expected 3, got {result4}"
    
    print("✅ All test cases passed!")
    
    # Test binary search approach
    print("\nTesting binary search approach:")
    test_cases = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([100], 1),
        ([0], 0),
        ([1, 2, 3, 4, 5], 3)
    ]
    
    for citations, expected in test_cases:
        result = hIndexBinarySearch(citations)
        print(f"citations = {citations}, h-index = {result}, expected = {expected}")
        assert result == expected, f"Binary search failed for {citations}"
    
    print("✅ Binary search approach also works correctly!")
