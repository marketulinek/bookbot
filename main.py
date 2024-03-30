def main():

    path_to_book = 'books/frankenstein.txt'

    # Print the book
    text = get_book_text(path_to_book)
    print(text)

    # Count the words
    num_words = get_num_words(text)
    print(f"{num_words} words found in the book.")

    # Statistics of chars
    num_chars = get_num_chars(text)
    print(num_chars)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
        return book_contents


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1
    return chars


main()
