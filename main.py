def main():

    path_to_book = 'books/frankenstein.txt'

    # Print the book
    text = get_book_text(path_to_book)
    print(text)

    # Count the words
    num_words = get_num_words(text)
    print(f"{num_words} words found in the book.")

    # Statistics of letter
    num_letters = get_num_letters(text)
    print(num_letters)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
        return book_contents


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    words = text.split()
    letter_stats = {}
    for word in words:
        lowered_word = word.lower()
        for letter in lowered_word:
            if letter not in letter_stats:
                letter_stats[letter] = 0
            letter_stats[letter] += 1
    return letter_stats


main()
