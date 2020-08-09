from hashtable import HashTable, HashTableEntry

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    results = []
    # Edge case of empty array, or array of length 1.

    if len(a) < 2:
        return False

    # Step 1: Sort input list

    sorted_list = sorted(a)

    # Step 2: Split into pos and neg lists

    pos_list = []
    neg_list = []


    for num in sorted_list:
        if num > 0:
            pos_list.append(num)
        elif num < 0: 
            neg_list.append(num)
    
    # Step 3: If there are no neg values, return empty list results.

    if len(neg_list) == 0:
        return results
    
    # Step 4: Create hashtable with capacity of pos or neg list with least num of values

    smaller = min([pos_list, neg_list], key=len)
    bigger = max([pos_list, neg_list], key=len)

    # Step 5: Make sure smaller and bigger are not the same list.
    if len(smaller) == len(bigger):
        smaller = neg_list
        bigger = pos_list
    
    # Step 6: Create a hashtable with the capacity of the length of list smaller.
    hash_table = HashTable(len(smaller))

    # Step 7: Add each value in smaller as hash table entry, key is str version of value

    for num in smaller:
        hash_table.put(str(abs(num)), True)

    # Step 8: Go through list bigger, and if able to find in hashtable, add val to results.
    for num in bigger:
        hash_entry = hash_table.get(str(abs(num)))
        if hash_entry is not None:
            results.append(abs(num))

    
    return results



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
