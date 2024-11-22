class Student:
    def __init__(self, firstname, lastname):    # self -> convention name
        self.firstname = firstname
        self.lastname = lastname

def main():
    st = Student("Bob", "M.")
    
    print("First name:", st.firstname)
    print("Last name:", st.lastname)

    st.hello_dimitris = "A re Mitso"

    print(st.hello_dimitris)    # can add variables and later in an object

if __name__ == "__main__":
    main()