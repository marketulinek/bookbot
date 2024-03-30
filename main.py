def main():

    path_to_book = 'books/frankenstein.txt'

    with open(path_to_book) as f:
        file_contents = f.read()
        print(file_contents)


main()
