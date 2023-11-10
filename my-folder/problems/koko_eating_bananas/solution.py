class Solution:
    def can_finish_eating(self, piles, h, k):
        hours_used = 0
        for p in piles:
            hours_used += ceil(float(p) / k)
        return hours_used <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1000000000
        min_speed = -1

        while left <= right:
            mid = (left + right) // 2
            if self.can_finish_eating(piles, h, mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_speed


        