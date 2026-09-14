"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for (index, value) in enumerate(lst):
        if target == value:
            return index
    return -1
##Linear search has a runtime complexity of O(N) because you have to check every single one in order with no shortcuts so if you were to double the list
##size it would automatically double the worst case work.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
    #When it comes to binary search each iteration drops the search space by half. It starts in the middle check to see if target is =,>,<,
    #if its less than it grabs the mid point of values before the first initial mid point and checks again(same thing if this is for a number greater than mid point).


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    #Small data set that is already sorted
    smallDataSet = [1,2,3,4,5,6,7,8,9,10]

    #linear test to search for value that is in the data set and print the index of which the value is found at
    print(f"Linear Test value 7 is found at Index: {linear_search(smallDataSet, 7)}")
    #linear test to search for value that is not in the data set and should return -1
    print(f"Linear test value 12 is found at Index: {linear_search(smallDataSet, 12)}")

    #binary search test for a value that is in the data set and should return the index of which value is found
    print(f"Binary Test value 7 is found at Index: {binary_search(smallDataSet, 7)}")
    #binary search test for a value that is not in the data set should return -1
    print(f"Binary test value 12 is found at Index: {binary_search(smallDataSet, 12)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    #Creating a blank list
    largeDataSet = []
    #for loop to enter value of index up to 50
    for index in range(50):
        largeDataSet.append(index)

    #test linear search for a value that is in the large data set and should return the index of which the value is found
    print(f"Linear Test value 38 is found at Index: {linear_search(largeDataSet, 38)}")
    #Test linear search for a value that is not in the large data set and should return -1
    print(f"Linear test value 72 is found at Index: {linear_search(largeDataSet, 72)}")

    #Test binary search for a value that is in the large data set and should return the index of which the value is found
    print(f"Binary test value 42 is found at Index: {binary_search(largeDataSet, 42)}")
    #Test binary search for a value that is not in the large data set and should return -1
    print(f"Binary test value 98 is found at Index: {binary_search(largeDataSet, 98)}")

    #as the data set grows much larger linear search must search every index starting at index 0 and has to go in order with no shortcuts or skips
    #With the linear search test being 38 that means it must iterate 39 times in order to finally find the target Meanwhile binary search cuts every iteration in half
    #for the example searching for 42 it completed 6 iterations and this was further down the list comparative to 38 in the linear test.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #Create an empty list
    emptyList = []
    #Linear test on the empty string should return a -1
    print(f"Linear Test on an empty list: {linear_search(emptyList, 0)}")
    #Binary test on an empty string should return a -1
    print(f"Binary Test on an empty list: {linear_search(emptyList, 1)}")

    #In both of these test cases since emptyList = 0 both of these loops never actually execute and the condition immediately fails returning -1

    singleElementList = [1]
    #linear test for a value that is within a single element list should return the index of value
    print(f"Linear Test on a single element: {linear_search(singleElementList, 1)}")
    #linear test for a value that is not within a single element list and should return -1
    print(f"Linear Test on a single element: {linear_search(singleElementList, 2)}")
    #Binary test on a value that is within a single element list shoudl return the index of the value
    print(f"Binary Test on a single element: {linear_search(singleElementList, 1)}")
    #BInary test on a value that is not within a single element list and should return -1
    print(f"Binary Test on a single element: {linear_search(singleElementList, 2)}")

    #For the test cases that do have the value within the list one iteration of the loops should execute before retuning the index of the value

    #For the test cases that do not have the value within the list one iteration is completed which then all conditions fail and -1 is returned


if __name__ == "__main__":
    main()