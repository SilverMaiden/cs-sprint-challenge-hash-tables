class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        used_count = 0
        for each in self.table:
            if each is not None:
                used_count += 1
        return used_count / self.capacity
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for each in key:
            hash = (hash * 33) + ord(each)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here -- should handle collisions

        newEntry = HashTableEntry(key, value)
        hash_key = self.hash_index(key)
       
        if self.get_load_factor() < 0.7 and hash_key < len(self.table):
            if self.table[hash_key] is None:
                self.table[hash_key] = newEntry
            else:
                current_node = self.table[hash_key]
                previous_node = None
                while current_node.key != key and current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next

                #IF current node's key is target key and there's a node behind it:
                if current_node.key == key and previous_node is not None:
                    previous_node.next = newEntry
                    newEntry.next = current_node.next
                #IF current node's key is target key and there's no node behind it:
                elif current_node.key == key and previous_node is None:
                    self.table[hash_key] = newEntry
                #IF current node's key is not target key and there's no node behind it:
                elif current_node.key != key and current_node.next is None:
                    current_node.next = newEntry
        else:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)
            self.put(key, value)





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_key = self.hash_index(key)
        if self.table[hash_key] is not None:
            current_node = self.table[hash_key]
            previous_key = None
            #Loop through linked list, looking for key and breaking loop
            #if key is found or reached end of list.
            while current_node.key != key and current_node.next is not None:
                previous_key = current_node
                current_node = current_node.next
            #IF current node's key is target key and there's a node behind it, and something in front:
            if current_node.key == key and previous_key is not None and current_node.next is not None:
                previous_key.next = current_node.next
            #IF current node's key is target key and there's no node behind it:
            elif current_node.key == key and previous_key is None and current_node.next is None:
                self.table[hash_key] = None
            #IF current node's key is target key and there's no node behind it but there is one in front:
            elif current_node.key == key and previous_key is None and current_node.next is not None:
                self.table[hash_key] = current_node.next
            #IF current node's key is not target key and there's no node behind it:
            elif current_node.key != key and current_node.next is None:
                return "Warning - Key not found."
        else:
            return "Warning - Key not found."


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_key = self.hash_index(key)
        if self.table[hash_key] is not None:
            current_node = self.table[hash_key]
            while current_node.key != key and current_node.next is not None:
                current_node = current_node.next

            if current_node.key == key:
                return current_node.value
            elif current_node.next is None:
                return None

        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        for entry in old_table:
            if entry is not None:
                self.put(entry.key, entry.value)


        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
