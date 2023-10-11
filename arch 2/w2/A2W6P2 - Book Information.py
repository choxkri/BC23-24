def add(storage: list):
    details = input("Book details: ").split(",")
    info = {
        "title" : details[0],
        "author" : details[1],
        "publisher" : details[2],
        "pub_date" : details[3]
    }
    for x in storage:
        if x["title"] == info["title"]:
            return
    storage.append(info)
    print("Book has been added")

def search(books: list, term: str) -> bool:
    for book in books:
        if term in book.values():
            return True
    return False

def main():
    #input example: lotr,tolkien,spectrum,1980
    library = []
    while True:
        print("[A] Add book")
        print("[S] Search book")
        print("[E] Exit")
        ui = input().upper()
        if ui == "A":
            add(library)

        if ui == "S":
            term_in = input("Search term: ")
            print(search(library, term_in))

        if ui == "E":
            for x in library: print(x)
            quit()



if __name__ == "__main__":
    main()