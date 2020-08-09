def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code 
    # Step 1: Create dictionary

    intersectionDictionary = {}
    LEN_KEY = len(arrays)

    # Step 2: Go through each array in arrays, if value is not in dict
    # then add to dict, otherwise increment value by 1
    for array in arrays:
        for num in array:
            if num not in intersectionDictionary:
                intersectionDictionary[num] = 1
            else:
                intersectionDictionary[num] += 1
    
    # Step 3: Make result list of keys in dictionary such that value = LEN_KEY
    result = [val[0]
              for val in list(intersectionDictionary.items()) if val[1] == LEN_KEY]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
