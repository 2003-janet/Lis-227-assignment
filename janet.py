class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def add_student(self, student):
        self.students.append(student)

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")

    def display_students(self):
        print("Students in the library:")
        for student in self.students:
            print(f"Name: {student['name']}")

def main():
    library = Library()

    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Add Student")
        print("3. Display Books")
        print("4. Display Students")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book = {'title': title, 'author': author}
            library.add_book(book)
            print("Book added successfully!")

        elif choice == '2':
            name = input("Enter student name: ")
            student = {'name': name}
            library.add_student(student)
            print("Student added successfully!")

        elif choice == '3':
            library.display_books()

        elif choice == '4':
            library.display_students()

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
