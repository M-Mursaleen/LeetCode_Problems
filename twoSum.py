from typing import List

nums = [1, 2, 3, 4]

for inner_val in range(len(nums)):
    print(inner_val)


def twoSum(nums: List[int], target: int) -> List[int]:
    initialTwoSum = nums[0] + nums[1]
    targeted_arr = []
    if initialTwoSum == target:
        return [0, 1]

    else:
        for val in range(len(nums)):
            if len(targeted_arr) == 0:
                for inner_val in range(val + 1, len(nums)):
                    if nums[val] + nums[inner_val] == target:
                        targeted_arr.append(val)
                        targeted_arr.append(inner_val)
                        break

    return targeted_arr


arr = [2, 5, 5, 11]
target = 10

twoSum(arr, target)
