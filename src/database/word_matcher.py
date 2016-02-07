import sqlite3

__author__ = "Aishwarya Sharma"


# Retreives a list of words from the database of a certain length
def get_words_from_db(length):
    # Making a connection with the database file
    connection = None
    words = []

    try:
        connection = sqlite3.connect("./database/words.db")
        cursor = connection.execute(
            "select word from words where (length = {0})".format(length))
        for row in cursor:
            words.append(row[0])
    except:
        pass
    finally:
        # Cleaning up the open connection
        if connection is not None:
            connection.commit()
            connection.close()

    return words


# Returns a list of words whose letters come under the char list and of a
# specific length
def get_matching_words(char_list, word_length):
    # Getting list of all possible words of specific length
    all_possible_words = get_words_from_db(word_length)

    possible_words = []

    # Checking to see if a word's letters are in char_list
    for word in all_possible_words:
        # Flag becomes false if some letter is not in char_list
        flag = True
        letters_in_word = list(word)
        letter_matching_list = list(char_list)

        # Sorting letters for faster matches
        letters_in_word.sort()
        letter_matching_list.sort()

        # Doing the matching
        for letter in letters_in_word:
            if letter not in letter_matching_list:
                flag = False
                break
            else:
                letter_matching_list.remove(letter)

        if flag is True:
            possible_words.append(word)

    return possible_words
