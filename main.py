def main():

    path_to_book = 'books/frankenstein.txt'

    # Print the book
    text = get_book_text(path_to_book)
    print(text)

    # Count the words
    num_words = get_num_words(text)
    print(f"{num_words} words found in the book.")


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
        return book_contents


def get_num_words(text):
    words = text.split()
    return len(words)


main()
