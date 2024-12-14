from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Defines the Student DAO API."""

    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()
        #pass

    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError()
    
    @abstractmethod
    def get_one(self, student_id):
        raise NotImplementedError()
    
class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student['id']
        self.students[student_id] = student
        print(f"Inserted student with id: {student_id}")

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found.")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found.")

    def get_one(self, student_id):
        return self.students.get(student_id, None)
    
class InventoryABC(ABC):
    
    @abstractmethod
    def add_item(self, item):
        """Add an item to the inventory."""
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        """Remove an item from the inventory."""
        pass

class Inventory(InventoryABC):
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_name_to_remove):
        """Remove an item from inventory by name."""
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item_name_to_remove)
                print(f"Removed item: {item_name_to_remove}")
                return
        print(f"Item not found: {item_name_to_remove}")

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
def main():
    student_impl = StudentImpl()
    student_impl.insert({'id':1, 'name':"Alice"})
    student_impl.insert({'id':2, 'name':"Bob"})
    student_impl.update(1, {'id':1, 'name':"SuperAlice"})
    print(student_impl.get_one(1))

    inventory = Inventory()
    item1 = Item("Laptop")
    item2 = Item("Phone")
    inventory.add_item(item=item1)
    inventory.add_item(item=item2)

if __name__ == '__main__':
    main()