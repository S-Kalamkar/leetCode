def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key = lambda interval: interval[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1],interval[1])
    return merged
    