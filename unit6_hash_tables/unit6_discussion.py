"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    dictionary = {}
    dictionary["Jenna"] = 90
    dictionary["Nick"] = 65
    dictionary["Dominique"] = 34
    dictionary["Chelsea"] = 76
    dictionary["Drew"] = 13
    #Dictionary behaves like a hash table because its pythons build in implementation of a hash table. Every time i add a key
    #dictionary["Nick"]=x python runs that key through a hash function which then converts it into a number which is then used to calculate the index to the array

    print(f'Dictionary: {dictionary}')


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")
    print(f"Lookup: {dictionary['Jenna']}")
    print(f"Lookup: {dictionary['Nick']}")
    #pythons build in dict function hashes the key which then goes to that index and then checks to verify that the key actually matches and then returns the value if key match = true

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    print(f"Dictionary before update: {dictionary}")
    dictionary["Dominique"] = 11
    print(f"Updated dictionary: {dictionary}")
    print(f"Dictionary before update: {dictionary}")
    dictionary["Chelsea"] = 67
    print(f"Updated dictionary: {dictionary}")
    #Since the key already exists python hashes is and then lands on the same exact index used the first time the key was added.
    #INstead of creating a new entry it just overwrites the value that was being stored. This allows the key to stay in place and only changes the value

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Dictionary before delete: {dictionary}")
    del dictionary["Jenna"]
    print(f"Deleted dictionary: {dictionary}")
    print(f"Dictionary before delete: {dictionary}")
    del dictionary["Drew"]
    print(f"Deleted dictionary: {dictionary}")
    #Similar to the  above instead of searching the whole list the key is hashed by python leading to the exact index in which the value and the key are then removed.
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")
    #Edge case 1 lookup a missing key
    try:
        print(f"Edge Case: {dictionary['Kaleb']}")
    except KeyError as e:
        print(f"Edge Case: KeyError: {e} does not exist in dictionary")
    #In this edge case the key is missing so up reaching this line of code a KeyError: 'Kaleb' Is thrown

    #Edge case 2 update  missing key
    dictionary["Kaleb"] = 10
    print(f"Edge Case: {dictionary['Kaleb']}")
    #in this case with updating a key that is missing python just adds it to the hashtable

if __name__ == "__main__":
    main()