# Your code here
from hashtable import HashTable, HashTableEntry

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = []

    # Check for edge case, queries is empty
    if queries == [] or files == []:
        print("hiiiii", queries, files)
        return results
    print(len(queries))
    hash_table = HashTable(len(queries) * 100)

    print("Started inserting")

    for query in queries:
        hash_table.put(query, True)
    
    print("finished inserting")

    for path in files:
        split_path = path.split("/")
        file_name = split_path[-1]
        hash_entry = hash_table.get(file_name)
        if hash_entry is not None:
            results.append(path)
    print("finished inserting results")

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
