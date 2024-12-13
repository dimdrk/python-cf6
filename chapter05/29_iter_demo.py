class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __repr__(self):
        return f"DataCollection({self.data})"

def main():
    collection = DataCollection([1, 2, 3, 4])

    print(f"Collection: {collection}")

    print("Iteration...")
    for item in collection:
        print(item, end=", ")
    print()

    print("Unpacking...")
    a, b, c, d = collection
    print(a, b, c, d)

    print("Indexing...")
    print(f"collection[1]: {collection[1]}")

    print("Slicing...")
    print(f"collection[1:3]: {collection[1:3]}")

    print(f"len(collection): {len(collection)}")

    # 1. for item in collection: ....
    # 2. a, b, c, d = collection
    # 3. collection[2]
    # 4. collection[1:3]
    # 5. len(collection)

if __name__ == '__main__':
    main()