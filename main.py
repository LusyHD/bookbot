import sys

from stats import (
    word_count,
    char_count,
    char_sort
)

def main():
    # HOW TO USE:
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        
        book_text = get_book_text(book_path)
        book_count = word_count(book_text)
        book_char = char_count(book_text)
        char_neat = char_sort(book_char)

        print_report(book_path, book_count, char_neat)
    else:
        print("---------- HOW TO USE ----------")
        print("Usage: python3 main.py <path_to_book>")
        print("--------------------------------")
        sys.exit(1)

# book text
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

# THE MEAT OF BOOKBOT
# report that includes:
# {book_path} file location of book
# {book_count} total number of words
# {dict_sort} loop to print every letter and its usage quantity
def print_report(book_path, book_count, char_neat):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for dict_sort in char_neat:
        if dict_sort["char"].isalpha():
            print(f"{dict_sort["char"]}: {dict_sort["num"]}")
        else:
            pass
    print("============= END ===============")

main()
