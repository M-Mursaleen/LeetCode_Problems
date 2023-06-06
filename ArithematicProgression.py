from typing import List

print("Welcome!")


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr = sorted(arr)
    previous = 0
    next_val = 0
    index_val = {}
    for value in range(len(arr)):
        previous = value
        next_val = value + 1
        if previous < len(arr) - 1 and next_val <= len(arr) - 1:
            check_arithematic_progression = arr[next_val] - arr[previous]
            index_val[str(check_arithematic_progression)] = check_arithematic_progression
        else:
            break
    if len(index_val) > 1:
        return False
    else:
        return True


arr = [3, 5, 1]

canMakeArithmeticProgression(arr)
