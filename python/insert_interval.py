from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        1. Ищем интервал, у которого конечное число меньше начального числа в new_interval;
        2. Формируем пересекающийся интервал new_interval:
         его конечное число должно быть строго больше начального числа интервала из intervals;
        3. Добавляем new_interval в конечный список;
        4. Добавляем оставшиеся интервалы в конечный список;
        """
        merged_intervals = []
        i = 0

        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged_intervals.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
            i += 1

        merged_intervals.append(new_interval)
        merged_intervals.extend(intervals[i:])

        return merged_intervals


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]

# result: [[1, 2], [3, 10], [12, 16]]
print(Solution().insert(intervals, new_interval))
