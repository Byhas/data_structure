import pickle


# Define the data structure (tree of hash tables)
class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.children = {}


class TreeHashTable:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, key, value):
        node = self.root
        for k in key:
            if k not in node.children:
                node.children[k] = TreeNode(k)
            node = node.children[k]
        node.value = value

    def search(self, key):
        node = self.root
        for k in key:
            if k not in node.children:
                return None
            node = node.children[k]
        return node.value

    def delete(self, key):
        def delete_helper(node, key1, depth=0):
            if node is None:
                return None
            if depth == len(key1):
                node.value = None
            else:
                node.children[key1[depth]] = delete_helper(node.children.get(key1[depth]), key1, depth + 1)
                if not node.children[key1[depth]]:
                    del node.children[key1[depth]]
            return node

        self.root = delete_helper(self.root, key)

    def get_all(self):
        def traverse(node):
            res = []
            if node.value is not None:
                res.append(node.value)
            for k in node.children:
                res.extend(traverse(node.children[k]))
            return res

        return traverse(self.root)


# Initialize the data structure
data_structure = TreeHashTable()

# Main program loop
while True:
    # Display menu options
    print("Enter your choice:")
    print("1- Add new student")
    print("2- Search for a student")
    print("3- Search for all students in specific years")
    print("4- Delete a student")
    print("5- Print all students")
    print("6- Exit")

    # Read user's choice
    choice = input()

    if choice == '1':
        # Read student's ID, name, and GPA
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        gpa = float(input("Enter student GPA: "))

        # Insert student record into data structure
        data_structure.insert(student_id, (name, gpa))

        print("Student added successfully")

    elif choice == '2':
        # Read student's ID
        student_id = input("Enter student ID: ")

        # Search for student in data structure
        student_record = data_structure.search(student_id)

        if student_record is not None:
            # Display student's name and GPA
            name, gpa = student_record
            print(f"Student found: {name}, {gpa}")
        else:
            print("Student not found")

    elif choice == '3':
        # Read year
        year = input("Enter year: ")

        # Search for all students in the given year
        year_records = [record for record in data_structure.get_all() if record[0][:4] == year]

        if len(year_records) > 0:
            # Display detailed information for all students
            print("Students in year " + year + ":")
            for record in year_records:
                print(f"{record[0]} - {record[1]}, {record[2]}")
        else:
            print("No students are in this year")

    elif choice == '4':
        # Read student's ID
        student_id = input("Enter student ID: ")
        # Delete student record from data structure
        try:
            # Delete student record from data structure
            data_structure.delete(student_id)
            print("Student deleted successfully")
        except KeyError:
            print("Student not found")

    elif choice == '5':
        # Print detailed information for all students
        all_records = data_structure.get_all()
        print("All students:")
        for record in all_records:
            print(f"{record[0]} - {record[1]}, {record[2]}")

    elif choice == '6':
        # Save data structure object to file using object serialization
        with open("data_structure.pkl", "wb") as f:
            pickle.dump(data_structure, f)

        print("Data saved successfully")
        break

    else:
        print("Invalid option, please try again")
