library = [
    {"id": 101, "title": "Python Basics",      "status": "available"},
    {"id": 102, "title": "Data Structures",    "status": "issued"},
    {"id": 103, "title": "Web Development",    "status": "available"},
    {"id": 104, "title": "Database Management","status": "issued"},
]

def show_all():
    print("=" * 40)
    print("       ALL BOOKS")
    print("=" * 40)
    for book in library:
        print(str(book["id"]) + " | " + book["title"] + " | " + book["status"].upper())

def available_books():
    print("=" * 40)
    print("     AVAILABLE BOOKS")
    print("=" * 40)
    for book in library:
        if book["status"] == "available":
            print(str(book["id"]) + " | " + book["title"])

def issued_books():
    print("=" * 40)
    print("       ISSUED BOOKS")
    print("=" * 40)
    for book in library:
        if book["status"] == "issued":
            print(str(book["id"]) + " | " + book["title"])

def summary():
    total = len(library)
    available = 0
    for book in library:
        if book["status"] == "available":
            available = available + 1
    print("=" * 40)
    print("Total    : " + str(total))
    print("Available: " + str(available))
    print("Issued   : " + str(total - available))
    print("=" * 40)

show_all()
available_books()
issued_books()
summary()
