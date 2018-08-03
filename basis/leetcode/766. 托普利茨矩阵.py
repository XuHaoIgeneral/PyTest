"""
    如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
示例 1:
输入:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < 1 or j < 1:
                    continue
                # print(f"x为{i} y为{j}")
                # print(matrix[i][j])
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


test = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
re = test.isToeplitzMatrix(matrix)
print(re)
