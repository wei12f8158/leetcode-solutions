# Common LeetCode Patterns

## 1. Two Pointers
**When to use**: Array/string problems, finding pairs, palindromes
**Examples**: Two Sum, Container With Most Water, Valid Palindrome

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
    return result
```

## 2. Sliding Window
**When to use**: Subarray/substring problems with fixed/variable window
**Examples**: Maximum Sum Subarray, Longest Substring Without Repeating Characters

```python
def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

## 3. Hash Map/Set
**When to use**: Frequency counting, lookups, duplicates
**Examples**: Two Sum, Group Anagrams, Valid Anagram

```python
def hash_map_solution(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Process based on frequency
    return result
```

## 4. Stack/Queue
**When to use**: LIFO/FIFO operations, monotonic stacks
**Examples**: Valid Parentheses, Daily Temperatures, Largest Rectangle

```python
def stack_solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return len(stack) == 0
```

## 5. Tree Traversal
**When to use**: Tree problems, path finding
**Examples**: Binary Tree Inorder Traversal, Path Sum

```python
def dfs(root):
    if not root:
        return
    
    # Preorder: process root
    dfs(root.left)
    # Inorder: process root
    dfs(root.right)
    # Postorder: process root

def bfs(root):
    if not root:
        return []
    
    queue = [root]
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 6. Dynamic Programming
**When to use**: Optimization problems, overlapping subproblems
**Examples**: Climbing Stairs, House Robber, Longest Increasing Subsequence

```python
def dp_solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## 7. Binary Search
**When to use**: Sorted arrays, searching in O(log n)
**Examples**: Search Insert Position, Find First and Last Position

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

## 8. Backtracking
**When to use**: Generate all possible solutions
**Examples**: Permutations, Combinations, N-Queens

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, updated_choices)
            path.pop()
```

## 9. Greedy
**When to use**: Local optimal choices lead to global optimum
**Examples**: Gas Station, Jump Game, Activity Selection

```python
def greedy_solution(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end_time = 0
    
    for start, end in intervals:
        if start >= end_time:
            count += 1
            end_time = end
    
    return count
```

## 10. Graph Algorithms
**When to use**: Network problems, connectivity
**Examples**: Course Schedule, Number of Islands, Clone Graph

```python
def dfs_graph(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    
    for neighbor in node.neighbors:
        dfs_graph(neighbor, visited)

def bfs_graph(start):
    queue = [start]
    visited = {start}
    
    while queue:
        node = queue.pop(0)
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## 11. Sorting + Greedy
**When to use**: Problems requiring optimal ordering with greedy selection
**Examples**: H-Index, Meeting Rooms II, Non-overlapping Intervals

```python
def h_index(citations):
    citations.sort(reverse=True)  # Sort in descending order
    h = 0
    
    for i, citation in enumerate(citations, 1):  # 1-indexed
        if citation >= i:
            h = i
        else:
            break  # Early termination since sorted
    
    return h

def meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end_time = 0
    
    for start, end in intervals:
        if start >= end_time:
            count += 1
            end_time = end
    
    return count
```

## 12. Greedy Reachability
**When to use**: Problems about reaching a target with optimal/maximum moves
**Examples**: Jump Game, Jump Game II, Gas Station

```python
def can_jump(nums):
    max_reach = 0  # Furthest position we can reach
    
    for i in range(len(nums)):
        if i > max_reach:
            return False  # Can't reach current position
        
        max_reach = max(max_reach, i + nums[i])
        
        # Early termination if we can reach the end
        if max_reach >= len(nums) - 1:
            return True
    
    return True

def jump_game_ii(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps
```
