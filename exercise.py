class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0

        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                return False
            count += 1

            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
        return True

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2

            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1

        return left
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for k in nums:
            if k in map:
                return True
            else:
                map[k] = True
        return False
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(res, root)
        return res

    def helper(self, res, root):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
            i += 1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, le, r):
            if le == r:
                return arr

            m = (le + r) // 2
            mergeSort(arr, le, m)
            mergeSort(arr, m + 1, r)
            merge(arr, le, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return None
    
        def helper(node: TreeNode, level: int) -> None:
            if len(res) == level:
                res.append([])

            res[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        return res
    
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return element
        
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.q1.append(element)
        return element

    def empty(self) -> bool:
        return not self.q1 and not self.q2


class Solution:
    def sucessor(self, root: TreeNode) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       if not root:
           return None

        if key > root.val:
           self.deleteNode(root.right, key)
        elif key < root.val:
           self.deleteNode(root.left, key)
        else:
            if not (root.right or root.left):
               root = None
            elif root.right:
                root.val = self.sucessor(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
    
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heap.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heapop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heapop(self.heap)
        return self.heap[0]
    
class Solution:
    def mergeTwo(self, list1, list2):
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       