def word_count(book_text):
    # {book_words} splits the {book_text} into single words
    # {total} counter variable
    book_words = book_text.split()
    total = 0

    # {book} counts each word and increments {total} by 1
    # return {total} word count
    for book in book_words:
        total += 1
    return total

def char_count(book_text):
    # dictionary & variables
    char_dict = {}
    low_text = book_text.lower()
    book_words = low_text.split()

    #####################################################################
    # {book} goes through each word in {book_words}                     #
    # {letters} breaks it down into single letters                      #
    # {i} checks to see if a letter exists in {char_dict} dictionary    #
    #   # if yes: increment counter by 1                                #
    #   # if no: set counter to 1                                       #
    # return dictionary of each letter with counter of quantity         #
    ######################################################################
    for book in book_words:
        letters = list(book)

        for i in letters:

            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    return char_dict

# sort for {char_sort}
def sort_on(dict):
    return dict["num"]

# takes {char_count} as input
# outputs the sorted list by {char_total}
def char_sort(char_count):
    sorted_list = []

    for char in char_count:
        char_total = char_count[char]

        temp_dict = {"char":char, "num":char_total}
        sorted_list.append(temp_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return(sorted_list)