# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        The approach involves iterating through the intervals and determining whether the current interval overlaps
        with the new interval. If it does, we merge them; otherwise, we place the new interval at the correct position
        in the sorted list.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not intervals:
            return [newInterval]
        res_intervals = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res_intervals.append(newInterval)
                    inserted = True
                res_intervals.append(interval)
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1]),
                ]
        if not inserted:
            res_intervals.append(newInterval)
        return res_intervals
