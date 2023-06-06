from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    initialTwoSum = nums[0] + nums[1]
    next_index = 0

    targeted_arr = []

    if initialTwoSum == target:
        return [0, 1]

    else:
        for val in range(1, len(nums) - 1):
            next_index = val + 1
            if nums[val] + nums[next_index] == target:
                targeted_arr.append(val)
                targeted_arr.append(next_index)

    return targeted_arr

arr = [3,2,4]
target = 6

twoSum(arr, target)