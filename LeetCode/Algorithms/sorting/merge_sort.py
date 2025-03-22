from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid_idx = len(arr) // 2
    left_side = arr[:mid_idx]
    right_side = arr[mid_idx:]

    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)

    return merge(merge_sort(left_sorted), merge_sort(right_sorted))

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        
    result.extend(left)
    result.extend(right)

    return result


#test code below
# unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
# unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
# unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

# ordered_list1 = merge_sort(unordered_list1)
# ordered_list2 = merge_sort(unordered_list2)
# ordered_list3 = merge_sort(unordered_list3)

# print(ordered_list1)
# print(ordered_list2)
# print(ordered_list3)