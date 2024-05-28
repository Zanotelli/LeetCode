from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        def check_bigger(n: int, sortd: List[int]):
            count = 0
            for s in range(len(sortd)-1, -1, -1):
                if n <= sortd[s]:
                    count += 1
                else:
                    return count
            return count
        nums_sort = sorted(nums)
        size = len(nums)
        for i in range(size):
            n = size-i
            if n == check_bigger(n, nums_sort):
                return n
        return -1

print(Solution().specialArray([3,6,7,7,0]))
