"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #Create a copy of the originial list
    tempList = lst[:]

    #Outer loop: Each pass bubbles the next largest unsorted element to its place
    for i in range(0, len(tempList) - 1):
        #Inner loop: Compare each pair of adjacent elements up to the unsorted
        for j in range(0, len(tempList) - 1 - i):
            if tempList[j] > tempList[j + 1]:
                #swap if out of order
                temp = tempList[j]
                tempList[j] = tempList[j + 1]
                tempList[j + 1] = temp
    return tempList



def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) > 1:
        #find the midpoint in the partition
        mid = len(lst) // 2

        left = merge_sort(lst[0:mid])
        right = merge_sort(lst[mid:])

        #merge left and right partition in sorted order
        return merge(left, right)
    return lst


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    mergedSize = len(left) + len(right)

    mergedNumbers = [0] * mergedSize
    mergePos = 0
    leftPos = 0
    rightPos = 0

    #Compare front of left and front of right and allocate the smaller value each time
    while leftPos < len(left) and rightPos < len(right):
        if left[leftPos] < right[rightPos]:
            mergedNumbers[mergePos] = left[leftPos]
            leftPos += 1
        else:
            mergedNumbers[mergePos] = right[rightPos]
            rightPos += 1
        mergePos += 1

    #Left has left over elements. right ran out first
    while leftPos < len(left):
        mergedNumbers[mergePos] = left[leftPos]
        leftPos += 1
        mergePos += 1

    #Right has left over elements. Left ran out first
    while rightPos < len(right):
        mergedNumbers[mergePos] = right[rightPos]
        rightPos += 1
        mergePos += 1
    return mergedNumbers


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    #Create an unsorted list with 7 values
    strengthsList = [24,3,6,18,9,12,16]

    #Print the originl list
    print(f"List of strengths: {strengthsList}")

    #Bubble sort and display output
    print(f"Bubble sort: {bubble_sort(strengthsList)}")

    #Print originial list
    print(f"Orignial list: {strengthsList}")

    #Merge sort and display output
    print(f"Merge Sort: {merge_sort(strengthsList)}")



    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    secondList = [847,-36,56,344,-178,29,14]
    print(f"Original List: {secondList}")

    #bubble sort and display
    print(f"Bubble sort: {bubble_sort(secondList)}")
    #Print original list
    print(f"Original List: {secondList}")
    #Merge sort and display
    print(f"Merge Sort: {merge_sort(secondList)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #First edge case on an empty list
    emptyList = []
    #Bubble sort and merge sort
    print(f"Original List: {emptyList}")
    print(f"Bubble sort: {bubble_sort(emptyList)}")
    #When it comes to a bubble sort the first loop otherwise known as the outer loop just doesnt execute and then returns the list. No error is thrown
    print(f"Original List: {emptyList}")
    print(f"Merge Sort: {merge_sort(emptyList)}")
    #When it comes to merge sort since the length of the list is not greater than 1 this skips recursion and returns the list. No erro is thrown

    #Edge case 2 with an already sorted list
    alreadySorted = [1,2,3,4,5,6,7]
    print(f"Original List: {alreadySorted}")
    print(f"Bubble sort: {bubble_sort(alreadySorted)}")
    #Bubble sort will still run the entire loop and compare everything it will just never end up swapping anything
    print(f"Original List: {alreadySorted}")
    print(f"Merge Sort: {merge_sort(alreadySorted)}")
    #Merge sort still splits into two groups and then merges back. Nothing changes







if __name__ == "__main__":
    main()