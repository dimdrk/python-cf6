import os

def read_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path} does not exist or is not valid file.")
        return
    
    try:
        with open(file_path, 'r') as f:
            # print some metadata
            print("Filename:", f.name)
            print("Closed:", f.closed)
            print("Opening mode:", f.mode)

            # read the file contents
            contents = f.read()
            print("Contents:", contents)
    except FileNotFoundError:
        print(f"Error file: {file_path} not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}: {e}")

    print("File closed after with-block:", f.closed)


def create_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            print(f"File {file_path} created with content: {content}")
    except IOError as e:
        print(f"Error creating file '{file_path}: {e}")

    
def update_file(file_path, content):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path} does not exist or is not valid file.")
        return
    
    try:
        with open(file_path, 'a') as f:
            f.write(content)
            print(f"File {file_path} updated successfully with new content.")
    except IOError as e:
        print(f"Error updating file '{file_path}: {e}")


def delete_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path} does not exist or is not valid file.")
        return
        
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully!")
    except IOError as e:
        print(f"Error deleting file '{file_path}: {e}")

def main():
    # Create a file
    create_file('test_cf6.txt', "This is my first text.")
    read_file('test_cf6.txt')

    update_file('test_cf6.txt', "Hello Python Masters!")

    delete_file('test_cf6.txt')

    read_file('test_cf6.txt')

if __name__ == '__main__':
    main()