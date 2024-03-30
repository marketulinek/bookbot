def main():

    path_to_book = 'books/frankenstein.txt'
    text = get_book_text(path_to_book)
    print(text)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
        return book_contents


main()
