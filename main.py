def main():

    path_to_book = 'books/frankenstein.txt'

    # Print the book
    text = get_book_text(path_to_book)
    print(text)

    # Count the words
    words_number = count_words(text)
    print('Number of  words in the book:', words_number)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
        return book_contents


def count_words(text):
    words = text.split()
    return len(words)


main()
