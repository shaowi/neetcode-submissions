class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        target_row = start - 1 # start is the index of the target next greater row
        start = 0
        end = len(matrix[0]) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False
        