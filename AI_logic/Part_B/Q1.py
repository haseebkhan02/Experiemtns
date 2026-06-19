"""You are given an integer array nums that was originally sorted in strictly ascending order but has been rotated at some unknown pivot index k. 
For example, [0, 1, 2, 4, 5, 6, 7] rotated at pivot index 4 becomes [4, 5, 6, 7, 0, 1, 2].

Write a function search(nums, target) that returns the index of target in nums, or -1 if target is not present.
Your solution must achieve O(log n) time complexity.

"""


def search(nums, target):
    # trying binary search 
    front, back = 0, len(nums)-1
    while front <= back: 
        mid = (front + back) //2
        if nums[mid] == target:
            return mid
        if nums[front] <= nums[mid]:
            if nums[front] <= target <= nums[mid]:
                back =  mid-1
            else:
                front = mid+1
        else:
            if nums[mid] < target <=nums[back]:
                front = mid+1
            else:
                back = mid-1
    return -1

#checking test cases with given input 
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
nums2 = [4, 5, 6, 7, 0, 1, 2]  
target2 = 3

print(search(nums1, target1))
print(search(nums2, target2))


# got output as expected 