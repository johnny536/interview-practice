def two_sum(nums: list[int], target: int) -> list[int]:
    """返回两个不同元素的下标。平均时间 O(n)，额外空间 O(n)。"""
    seen: dict[int, int] = {}  # 数值 -> 之前出现的位置

    for index, num in enumerate(nums):
        complement = target - num

        # 先查找，再记录当前元素，避免重复使用同一个下标。
        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    # 题目保证存在答案；此分支用于处理不符合约束的输入。
    raise ValueError("没有找到和为 target 的两个元素")
