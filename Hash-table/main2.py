class ChainingHashTable:  # Hashing Class with separate chaining

    def __init__(self, initial_capacity=10):

        self.table = []  # Initialize the hash table with empty bucket list entries
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table, or updates an existing item
    def insert(self, key, item):  # Does both insert and update

        # Get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if self.search(key):
            return print(f"Ключ {key} вже зайнятий")

        # Update the key if it is already in the bucket list
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)   
        return True

    # Searches for an item with matching key in the hash table
    # Returns the item if found, or None if not found

    def search(self, key):
        # Get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # Search for the key in the bucket list
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                return kv[1]  # Value
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # Get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the item from the bucket list if it is present
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


    def display_hash(self): 
        for i in range(len(self.table)):
            print(i, end = " ")  
            for j in self.table[i]:
                print("-->", end = " ")
                print(j[1], end = " ")    
            print()
            

packageHash = ChainingHashTable()

# packageHash.insert(4, 4)
# packageHash.insert(1, 4)
# packageHash.insert(8, 6)
# packageHash.insert(5, 7)
# packageHash.insert(3, 2)
# packageHash.insert(9, 9)
# packageHash.insert(9, 8)
# item1 = packageHash.search(5)
# print(f"Знайдений елемент - {item1}")
# print("----------------------------")
# packageHash.remove(5)
# item1 = packageHash.search(5)
# print(f"Знайдений елемент - {item1}")
# print("----------------------------")
# # print(packageHash.table)
# packageHash.display_hash()

while(True):
        x=int(input('Choose option\n1) Insert\n2) Delete\n3) Search\n4) Show hash table\n5) Break\n'))
        if x==0:
                packageHash.insert(4, 4)
                packageHash.insert(1, 4)
                packageHash.insert(8, 6)
                packageHash.insert(5, 7)
                packageHash.insert(3, 2)
                packageHash.insert(9, 8)
                packageHash.display_hash()
        elif x==1:
                try:
                        key=int(input('Put for insert key = '))
                        value=int(input('Put for insert value = '))
                        packageHash.insert(key, value)
                        print('\n\n\n')
                        # packageHash.display_hash()
                except ValueError:
                        print("error!")            
        elif x==2:
                a=int(input("Key for delete = "))
                packageHash.remove(a)
                print('\n\n\n')
                # packageHash.display_hash()
        elif x==3:
                a=int(input('Put key for searh '))
                print(packageHash.search(a))
                print('\n\n\n')
                # packageHash.display_hash()
        elif x==4:
                packageHash.display_hash()
        elif x==5:
                break