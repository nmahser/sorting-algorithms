
nums = [4, 2, 3, 4, 6, 1, 4, 6, 7]

# ascending bubble sort


def bubbleSortAsc(nums):
    # iterates thru the array n times regardless if the array is already sorted
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums


print(bubbleSortAsc(nums))

# Optimized solution, but the worst case scenario is still O(n^2)


def bubbleSortAsc2(nums):
    # stop iterating when there is no swap
    swapped = True

    while(swapped):
        swapped = False

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

                swapped = True

        return nums


print(bubbleSortAsc2(nums))
