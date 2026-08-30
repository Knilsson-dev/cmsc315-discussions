"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    #using .insert will automatically walk through the list to the correct index and moves and copies the current value into the next slot over, inserts the new value and shifts all the following values up an index
    #the lower the index the better the performance. the higher the index the more iterations the computer has to go through in order to find the correct index.
    lst.insert(index, value)




def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    #validation before deleting is important because pop() will raise and indexError and crash the program
    #by validating first we are able to fail safely
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)



def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for index in range(len(lst)):
        if lst[index] == value:
            return index
        else:
            index
    return -1





def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    lst = [1,2,3,4,5,6,7]


    # 2. Display the original list.
    print(f"{lst}")

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # 3. Test insertion at:
    #    - the beginning and print list
    insert_at(lst, 0, 0)
    print(f"{lst}")

    #    - the middle and print list
    insert_at(lst, 4, 0)
    print(f"{lst}")

    #    - the end and print list
    insert_at(lst, 9, 0)
    print(f"{lst}")




    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Requirements:
    # 1. Delete an item from:
    #    - the beginning and print the deleted value and then print the updated list
    print(f"Removed value is {delete_at(lst, 0)}")
    print(f"{lst}")
    #    - the middle and print the deleted value and then print the updated list
    print(f"Removed value is {delete_at(lst, 3)}")
    print(f"{lst}")

    #    - the end and print the deleted value and then print the updated list
    print(f"Removed value is {delete_at(lst, 5)}")
    print(f"{lst}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Requirements:
    # 1. Search for a value that exists and print the index
    print(f"Value found at index (-1 == Null): {search_value(lst, 5)}")

    # 2. Search for a value that does not exist should return -1
    print(f"Value found at index (-1 == Null): {search_value(lst, 6)}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # - Delete using an invalid index and print what is deleted. None should be printed for invalid index
    print(f"Delete at invalid index: {delete_at(lst, 8)}")

    # - Search for a missing value and print the results. -1 Should be returned for an invalid index
    print(f"Search for a missing value: {search_value(lst, 8)}")




if __name__ == "__main__":
    main()