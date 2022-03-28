def print_upper_words(words, must_start_with):
    """Print capitalized words on a separate line for each word"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=["h", "y"])