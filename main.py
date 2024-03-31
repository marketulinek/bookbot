def main():

    path_to_book = 'books/frankenstein.txt'
    text = get_book_text(path_to_book)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    char_stats = wrap_dict_by_list(num_chars)
    char_stats.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{num_words} words found in the document\n")

    for char in char_stats:
        if char['char'].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times")

    print("--- End report ---")


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


def wrap_dict_by_list(dict_chars):
    new_list = []
    for char, num in dict_chars.items():
        new_dict = {'char': char, 'num': num}
        new_list.append(new_dict)
    return new_list


def sort_on(dict_chars):
    return dict_chars['num']


main()
