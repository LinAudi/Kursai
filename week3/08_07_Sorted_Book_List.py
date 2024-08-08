print("Sorted Book List: \n")

book_list = []
book_number = int(input("Enter number of books: "))

def book_info(title, author):
    info = {"Title:": title,"Author:":author}
    book_list.append(info)
    return info


for _ in range(book_number):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_info(title,author)

sorted_book_list = sorted(book_list, key=lambda x: x["Author:"])

print(f"Sorted books: {sorted_book_list}")
