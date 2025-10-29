# Library Management System
books = {}  # Dictionary: {ISBN: (title, author, genre, total_copies)}
members = []  # List: [(member_id, name, email, borrowed_books), ...]
genres = ("Fiction", "Non-Fiction", "Sci-Fi")  # Tuple of valid genres


def add_book(isbn, title, author, genre, total_copies):
    """Add a new book to the library."""
    if isbn in books:
        print("Error: ISBN already exists.")
        return
    if genre not in genres:
        print("Error: Invalid genre.")
        return
    if total_copies < 0:
        print("Error: Total copies cannot be negative.")
        return
    books[isbn] = (title, author, genre, total_copies)
    print(f"Book '{title}' added successfully with ISBN {isbn}.")


def add_member(member_id, name, email):
    """Add a new member to the library."""
    for member in members:
        if member[0] == member_id:
            print("Error: Member ID already exists.")
            return
    members.append((member_id, name, email, []))
    print(f"Member '{name}' added successfully with ID {member_id}.")


def search_book(query):
    """Search for books by title or author."""
    results = [
        (isbn, title, author, genre, total_copies)
        for isbn, (title, author, genre, total_copies) in books.items()
        if query.lower() in title.lower() or query.lower() in author.lower()
    ]
    if results:
        for isbn, title, author, genre, total_copies in results:
            print(f"Found: ISBN {isbn}, Title: {title}, Author: {author}, Genre: {genre}, Copies: {total_copies}")
    else:
        print("No books found matching the query.")


def update_book(isbn, title, author, genre, total_copies):
    """Update book details."""
    if isbn not in books:
        print("Error: ISBN does not exist.")
        return
    if genre not in genres:
        print("Error: Invalid genre.")
        return
    if total_copies < 0:
        print("Error: Total copies cannot be negative.")
        return
    books[isbn] = (title, author, genre, total_copies)
    print(f"Book with ISBN {isbn} updated successfully.")


def delete_book(isbn):
    """Delete a book from the library."""
    if isbn not in books:
        print("Error: ISBN does not exist.")
        return
    books.pop(isbn)
    print(f"Book with ISBN {isbn} deleted successfully.")


def borrow_book(member_id, isbn):
    """Allow a member to borrow a book."""
    member_found = None
    for member in members:
        if member[0] == member_id:
            member_found = member
            break
    if not member_found:
        print("Error: Member ID does not exist.")
        return
    if isbn not in books:
        print("Error: ISBN does not exist.")
        return
    title, author, genre, total_copies = books[isbn]
    if total_copies <= 0:
        print("Error: No copies available to borrow.")
        return
    books[isbn] = (title, author, genre, total_copies - 1)
    member_found[3].append(isbn)
    print(f"Book with ISBN {isbn} borrowed by member {member_id} successfully.")


def return_book(member_id, isbn):
    """Allow a member to return a book."""
    member_found = None
    for member in members:
        if member[0] == member_id:
            member_found = member
            break
    if not member_found:
        print("Error: Member ID does not exist.")
        return
    if isbn not in books:
        print("Error: ISBN does not exist.")
        return
    title, author, genre, total_copies = books[isbn]
    if isbn not in member_found[3]:
        print("Error: Member did not borrow this book.")
        return
    books[isbn] = (title, author, genre, total_copies + 1)
    member_found[3].remove(isbn)
    print(f"Book with ISBN {isbn} returned by member {member_id} successfully.")


# Demo
def run_demo():
    """Demonstrate the Mini Library Management System."""
    print("--- Demo: Mini Library Management System ---")

    # Add books
    add_book("123", "Beauty and the Beast", "Gabrielle-Suzanne Barbot de Villeneuve", "Fiction", 5)
    add_book("124", "Sci-Fi Adventures", "nico robin", "Sci-Fi", 3)

    # Add members
    add_member("M001", "Kenneth", "kenneth@email.com")
    add_member("M002", "itachi uchiha", "itachi@email.com")

    # Search for a book
    print("\nSearching for 'Beauty'...")
    search_book("Beauty")

    # Borrow a book
    print("\nBorrowing book 123 by M001...")
    borrow_book("M001", "123")

    # Return a book
    print("\nReturning book 123 by M001...")
    return_book("M001", "123")

    # Delete a book
    print("\nDeleting book 124...")
    delete_book("124")

    # Update a book
    print("\nUpdating book 123...")
    update_book("123", "Advanced Beauty and the Beast", "Gabrielle-Suzanne Barbot de Villeneuve", "Fiction", 4)


if __name__ == "__main__":
    run_demo()