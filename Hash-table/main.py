class HashTables: 

    def __init__(self):
        self.table = [[] for _ in range(10)]

    def hash(string):
      tmp = 5381
      byte_array = string.encode('utf-8')
      for byte in byte_array:
          tmp = ((tmp * 33) ^ byte) % 0x100000000
      return tmp


    def ChainedHashShow(self):
      for i in range(len(self.table)):
        print(i, end = " ")
        for j in self.table[i]:
          print("-->", end = " ")
          print(j, end = " ")	
        print()


    def ChainedHashInsert(self, keyvalue, value):
      hash_key = keyvalue % len(self.table)
      self.table[hash_key].append(value)

    def ChainedHashDelete(self, keyvalue, value):
        hash_key = keyvalue % len(self.table)
        if self.table[hash_key]:
                print(f"Значення {value} видалено")
                self.table[hash_key].remove(value)
        else:
                print("Nothing")


    def ChainedHashSearch(self, keyvalue):
      hash_key = keyvalue % len(self.table)
      return self.table[hash_key]

HashTable = HashTables()
# HashTable.ChainedHashInsert(10, 'Andriy')
# HashTable.ChainedHashInsert(25, 'Vitalii')
# HashTable.ChainedHashInsert(20, 'Artem')
# HashTable.ChainedHashInsert(20, 'Oleg')
# HashTable.ChainedHashInsert(9, 'Maxim')
# HashTable.ChainedHashInsert(21, 'Sasha')
# HashTable.ChainedHashInsert(21, 'Vova')
# HashTable.ChainedHashShow()
# print("----------------------------------")
# HashTable.ChainedHashDelete(10)
# print("----------------------------------")
# HashTable.ChainedHashShow()
# item1 = HashTable.ChainedHashSearch(25)
# print(item1)

while(True):
        x=int(input('Choose option\n1) Insert\n2) Delete\n3) Search\n4) Show hash table\n5) Break\n'))
        if x==0:
                HashTable.ChainedHashInsert(10, 'Andriy')
                HashTable.ChainedHashInsert(25, 'Vitalii')
                HashTable.ChainedHashInsert(20, 'Artem')
                HashTable.ChainedHashInsert(20, 'Oleg')
                HashTable.ChainedHashInsert(9, 'Maxim')
                HashTable.ChainedHashInsert(21, 'Sasha')
                HashTable.ChainedHashInsert(31, 'Vova')
                HashTable.ChainedHashShow()
        elif x==1:
                try:
                        key=int(input('Put for insert key = '))
                        value=int(input('Put for insert value = '))
                        HashTable.ChainedHashInsert(key, value)
                        print('\n\n\n')
                        # HashTable.ChainedHashShow()
                except ValueError:
                        print("error!")      
        elif x==2:
                try:
                        key=int(input('Put for delete key = '))
                        if len(HashTable.ChainedHashSearch(key)) == 0:
                                print('Value avoid')
                                break
                        value=input('Put for delete value = ')
                        HashTable.ChainedHashDelete(key, value)
                        print('\n\n\n')
                        # HashTable.ChainedHashShow()
                except ValueError:
                        print("error!")   
        elif x==3:
                a=int(input('Put key for searh '))
                print(HashTable.ChainedHashSearch(a))
                print('\n\n\n')
                # packageHash.display_hash()
        elif x==4:
                HashTable.ChainedHashShow()
        elif x==5:
                break
