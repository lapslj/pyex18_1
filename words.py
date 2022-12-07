

def print_upper_words(word_list,must_start_with):
    print_words = []
    for starter in must_start_with:
        add_words = [word.upper() for word in word_list if word.startswith(starter) == True]
        print(add_words)
        print_words = [*print_words,*add_words]
    return print_words


test1 = print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
# this should print "HELLO", "HEY", "YO", and "YES"

test2 = print_upper_words(["apple","car","bacon","food","bart","astronaut"],
                   must_start_with={"a", "b"})

"""
Do this work in a new file, words.py.

For a list of words, print out each word on a separate line, but in all uppercase. 
How can you change a word to uppercase? Ask Python for help on what you can do with strings!

Turn that into a function, print_upper_words. Test it out. 
(Don’t forget to add a docstring to your function!)

Change that function so that it only prints words that start with the letter ‘e’ 
(either upper or lowercase).

Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

For example:
"""
