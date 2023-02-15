import bisect


class BinarySearch:
    def __init__(self, data: list[int]) -> None:
        self.data = sorted(data)

    def binary_search_loop(self, target: int) -> int:
        if not self.data:
            return -1

        left: int = 0
        right: int = len(self.data) - 1

        while left <= right:
            mid: int = left + (right - left) // 2

            if self.data[mid] < target:
                left = mid + 1
            elif self.data[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    def binary_search_recursive(self, target: int) -> int:
        def recursive_search(left: int, right: int) -> int:
            if left > right:
                return -1

            mid: int = left + (right - left) // 2

            if self.data[mid] < target:
                return recursive_search(mid + 1, right)
            elif self.data[mid] > target:
                return recursive_search(left, mid - 1)
            else:
                return mid

        return recursive_search(0, len(self.data) - 1)

    def binary_search_bisect(self, target: int) -> int:
        index: int = bisect.bisect_left(self.data, target)

        if index != len(self.data) and self.data[index] == target:
            return index
        else:
            return -1
